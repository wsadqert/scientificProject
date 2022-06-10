from __future__ import annotations

from math import acos, log10, pi, sqrt, cos, sin, degrees, radians
from typing import Final

from scipy.interpolate import interp1d

from data.constants import *

import modeling.star as star


def calculate_transit(star_system: star.StarSystem, star_front: star.Star, star_back: star.Star) -> dict[str, float]:
	"""Calculates absolute magnitude of star system at transit time"""
	
	if (star_front != star_system.star1 and star_front != star_system.star2) or \
		(star_back != star_system.star1 and star_back != star_system.star2):
		raise AttributeError
	
	if star_front.radius >= star_back.radius:
		return {'L': star_front.L, 'magnitude': star_front.abs_magnitude}
	
	L_total: Final[float] = star_front.L + star_back.L * (star_back.square - star_front.square) / star_back.square
	abs_magnitude: Final[float] = abs_magnitude_sun - log10(L_total / L_sun) / 0.4
	return {'L': L_total, 'magnitude': abs_magnitude}


def calculate_touch(star_system: star.StarSystem, star_front: star.Star, star_back: star.Star, x: float) -> dict[str, float]:
	def calculate_intersection(R1: float, R2: float, D: float):
		"""R1 <= R2"""
		# see `/src/intersection.gif`, `/src/geometry_solution.jpeg`
		
		def calculate_cos_theorem(r1: float, r2: float, d: float):
			return degrees(acos((d**2 + r1**2 - r2**2)/(2*d*r1)))
		
		alpha1: float = calculate_cos_theorem(R1, R2, D)
		alpha2: float = calculate_cos_theorem(R2, R1, D)
		
		# print(alpha1, alpha2)

		S_sector_1: float = (alpha1 * pi * R1**2) / 360
		S_sector_2: float = (alpha2 * pi * R2**2) / 360
		
		S_triangle1: float = 1/2 * R1**2 * cos(radians(alpha1)) * sin(radians(alpha1))
		S_triangle2: float = 1/2 * R2**2 * cos(radians(alpha2)) * sin(radians(alpha2))
		
		A1: float = S_sector_1 - S_triangle1
		A2: float = S_sector_2 - S_triangle2
		
		return 2 * (A1 + A2)
	
	calculate_touch.calculate_intersection = calculate_intersection
	
	if (star_front != star_system.star1 and star_front != star_system.star2) or \
		(star_back != star_system.star1 and star_back != star_system.star2):
		from ctypes import ArgumentError
		raise ArgumentError
	
	if x <= abs(star_front.radius - star_back.radius):
		# see `/src/image_1.png`
		return star_system.calculate_transit(star_front, star_back)
	
	if star_front.radius + star_back.radius <= x:
		# see `/src/image_2.png`
		return {'L': star_system.L, 'magnitude': star_system.abs_magnitude}
	
	# see `/src/image_3.png`
	
	max_radius = max(star_front.radius, star_back.radius)
	min_radius = min(star_front.radius, star_back.radius)
	
	interpolator = interp1d((0, star_back.square), (star_back.L, 0))
	
	L_total: Final[float] = star_front.L + interpolator(calculate_intersection(min_radius, max_radius, x))
	abs_magnitude: Final[float] = star.abs_magnitude(L_total)
	
	return {'L': L_total, 'magnitude': abs_magnitude}
