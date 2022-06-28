from __future__ import annotations
import modeling.star as star
from modeling.calculations import calculate_intersection, interpolate
from data.constants import *


def calculate_transit(star_system: star.StarSystem, star_front: star.Star, star_back: star.Star) -> float:
	"""Calculates absolute magnitude of star system at transit time"""
	
	if (star_front != star_system.star1 and star_front != star_system.star2) or \
		(star_back != star_system.star1 and star_back != star_system.star2):
		raise AttributeError
	
	if star_front.radius >= star_back.radius:
		return star_front.abs_magnitude
	
	L_total: Final[float] = star_front.L + star_back.L * (star_back.square - star_front.square) / star_back.square
	abs_magnitude: Final[float] = abs_magnitude_sun - log10(L_total / L_sun) / 0.4
	return abs_magnitude


def calculate_touch(star_system: star.StarSystem, star_front: star.Star, star_back: star.Star, x: float) -> float:
	if not ((star_front in star_system) and (star_back in star_system)):
		from ctypes import ArgumentError
		raise ArgumentError
	
	if x <= abs(star_front.radius - star_back.radius):
		# see `/src/picture_in.png`
		return star_system.calculate_transit(star_front, star_back)
	
	if star_front.radius + star_back.radius <= x:
		# see `/src/picture_out.png`
		return star_system.abs_magnitude
	
	# see `/src/picture_intersection.png`
	
	max_radius = max(star_front.radius, star_back.radius)
	min_radius = min(star_front.radius, star_back.radius)
	
	L_total: Final[float] = star_front.L + interpolate(calculate_intersection(min_radius, max_radius, x), ((0, star_back.L), (star_back.square, 0)))
	abs_magnitude: Final[float] = star.abs_magnitude(L_total)
	
	return abs_magnitude
