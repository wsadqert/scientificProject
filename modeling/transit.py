from __future__ import annotations

from math import acos, degrees, log10, pi, sqrt
from typing import Final

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
		# see `/src/intersection.gif`, `/src/geometry_solution.png`
		
		O2C: float = (- R1**2 + R2**2 + D**2) / (2*D)
		
		out: bool = D >= R2
		
		if out:
			O1C: float = (+ R1**2 - R2**2 + D**2) / (2*D)
		else:
			O1C: float = (- R1**2 + R2**2 - D**2) / (2*D)

		S_triangle1: float = sqrt(R1**2 - O1C**2) * (O1C / 2)
		S_triangle2: float = sqrt(R2**2 - O2C**2) * (O2C / 2)
		
		alpha1: float = degrees(acos(O1C / R1))
		alpha2: float = degrees(acos(O2C / R2))
		
		if not out:
			alpha1 = 180 - alpha1
		
		S_sector_1: float = pi * R1**2 * (2 * alpha1)/360
		S_sector_2: float = pi * R2**2 * (2 * alpha2)/360
		
		if out:
			return (S_sector_1 - S_triangle1) + (S_sector_2 - S_triangle2)
		else:
			return (S_sector_1 - S_triangle1) + (S_sector_2 + S_triangle2)
	
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
	
	L_total: Final[float] = star_front.L + star_back.L * (star_back.square - calculate_intersection(min_radius, max_radius, x)) / star_back.square
	abs_magnitude: Final[float] = star.abs_magnitude(L_total)
	
	return {'L': L_total, 'magnitude': abs_magnitude}
