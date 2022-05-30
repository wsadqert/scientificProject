from __future__ import annotations

from math import log

from astropy.constants.iau2015 import L_sun

import modeling.star as st
from data.constants import *


def calculate_transit(star_front: st.Star, star_back: st.Star) -> dict[str, float]:
	"""Calculates absolute magnitude of star system at transit time"""
	
	if star_front.radius >= star_back.radius:
		return {'L': star_front.L, 'magnitude': star_front.abs_magnitude}
	
	L_total: float = star_front.L + star_back.L * (star_back.square - star_front.square) / star_back.square
	abs_magnitude = abs_magnitude_sun - log(L_total / L_sun.value) / 0.4
	return {'L': L_total, 'magnitude': abs_magnitude}


def calculate_touch(star_front: st.Star, star_back: st.Star, x: int | float) -> dict[str, float]:
	pass
