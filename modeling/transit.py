from typing import Tuple

import modeling.star as star
from modeling.calculations import calculate_intersection, interpolator, limb_darkening_interpolator
from data.constants import *


def calculate_transit(star_system, star_front, star_back) -> float:
	"""
	:param star_system: modeling.star.StarSystem
	:param star_front: modeling.star.Star
	:param star_back: modeling.star.Star
	"""
	if not ((star_front in star_system) and (star_back in star_system)):
		from ctypes import ArgumentError
		raise ArgumentError
	
	if star_front.radius >= star_back.radius:
		return star_front.L * (1 + limb_darkening_y) / 2
	
	L_total: float = star_front.L * (1 + limb_darkening_y) / 2 + star_back.L * (star_back.square - star_front.square) / star_back.square * (1 + limb_darkening_y) / 2
	
	abs_magnitude: Final[float] = abs_magnitude_sun - log10(L_total / L_sun) / 0.4
	return L_total


def calculate_touch(star_system, star_front, star_back, x: float) -> tuple[float, ...] | tuple[float, float]:
	"""
	:param star_system: modeling.star.StarSystem
	:param star_front: modeling.star.Star
	:param star_back: modeling.star.Star
	"""
	if not ((star_front in star_system) and (star_back in star_system)):
		from ctypes import ArgumentError
		raise ArgumentError
	"""
	if x <= abs(star_front.radius - star_back.radius):
		# see `/src/picture_in.png`
		return star_system.calculate_transit(star_front, star_back)
	"""
	if star_front.radius + star_back.radius <= x:
		# see `/src/picture_out.png`
		return tuple([star.abs_magnitude(star_system.L * (1 + limb_darkening_edge) / 2),]) * 2
	
	# see `/src/picture_intersection.png`
	
	max_radius: float = max(star_front.radius, star_back.radius)
	min_radius: float = min(star_front.radius, star_back.radius)
	
	L_front: float = star_front.L * (1 + limb_darkening_edge) / 2
	L_back: float = star_back.L * (1 + limb_darkening_edge) / 2
	L_corr_square: float = interpolator((0, star_back.square), (0, star_back.L), calculate_intersection(min_radius, max_radius, x))
	L_corr_limb_darkening: float = limb_darkening_interpolator((max_radius + min_radius - x) / (4 * star_back.radius))
	# print(L_corr)
	
	L_total: float = L_front + L_back - L_corr_square * L_corr_limb_darkening
	
	# L_total: Final[float] = star_front.L * (1 + limb_darkening_y) / 2 + interpolate(calculate_intersection(min_radius, max_radius, x), ((0, star_back.L * (1 + limb_darkening_y) / 2), (star_back.square, 0)))
	abs_magnitude: float = star.abs_magnitude(L_total)
	
	# return L_corr
	# return L_corr_limb_darkening
	return abs_magnitude, star.abs_magnitude(L_front + L_back - L_corr_square)
