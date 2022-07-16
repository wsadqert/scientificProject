from data.constants import *
from scipy import interpolate as interp


def limb_darkening_interpolator(d: float):
	return interp.interp1d(limb_darkening_x, limb_darkening_y)(d)


interpolator = lambda x, y, d: interp.interp1d(x, y)(d)
