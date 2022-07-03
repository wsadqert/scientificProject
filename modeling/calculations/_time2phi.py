from data.constants import *

__all__ = ['circular_orbit', 'elliptical_orbit', 'time2phi']


def circular_orbit(t: float, T: float) -> float:
	return t / T * 360


def elliptical_orbit(t: float, T: float, e: float) -> float:
	M: float = t / T * 2*pi
	E: float = M
	
	for n in range(20):
		E = e * sin(E) + M
	
	phi: float = 2 * degrees(atan(tan(E/2) / sqrt((1-e) / (1+e))))
	
	if t/T > 0.5:
		phi += 360
	
	return phi


def time2phi(t: float, T: float, e: float) -> float:
	if e == 0:
		return circular_orbit(t, T)
	return elliptical_orbit(t, T, e)
