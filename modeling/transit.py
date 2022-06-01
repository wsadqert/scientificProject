from __future__ import annotations

from math import log
from typing import Final

from astropy.constants.iau2015 import L_sun

import modeling.star as st
from data.constants import *


def calculate_transit(star_front: st.Star, star_back: st.Star) -> dict[str, float]:
	"""Calculates absolute magnitude of star system at transit time"""
	
	if star_front.radius >= star_back.radius:
		return {'L': star_front.L, 'magnitude': star_front.abs_magnitude}
	
	L_total: Final[float] = star_front.L + star_back.L * (star_back.square - star_front.square) / star_back.square
	abs_magnitude: Final[float] = abs_magnitude_sun - log(L_total / L_sun.value) / 0.4
	return {'L': L_total, 'magnitude': abs_magnitude}


def calculate_touch(star_system: st.StarSystem, star_front: st.Star, star_back: st.Star, x: float) -> dict[str, float]:
	if (star_front != star_system.star1 and star_front != star_system.star2) or \
			(star_back != star_system.star1 and star_back != star_system.star2):
		raise AttributeError

	if star_front.radius < abs(star_front.radius - star_back.radius):
		# see `src/image_1.png`
		return calculate_transit(star_front, star_back)

	if star_front.radius + star_back.radius < star_front.radius:
		# see `src/image_2.png`
		return {'L': star_system.L, 'magnitude': star_system.abs_magnitude}
	
	L_total: Final[float] = ...
	abs_magnitude: Final[float] = ...

	return {'L': L_total, 'magnitude': abs_magnitude}
