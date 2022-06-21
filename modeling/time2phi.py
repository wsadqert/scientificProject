from data.constants import *

__all__ = ['circular_orbit', 'elliptical_orbit']


def circular_orbit(t: float, T: float) -> float:
	return t / T * 360


def elliptical_orbit(t: float, T: float, e: float) -> float:
	if e == 0:
		return circular_orbit(t, T)

	assert 0 < e < 1
	
	E: float = 0
	M: float = t / T * 2*pi
	
	for n in range(100):
		E = e * sin(E) + M
	
	phi: float = 2 * degrees(atan(tan(E/2) / sqrt((1-e) / (1+e))))
	
	if t/T > 0.5:
		phi += 360
	
	return phi
