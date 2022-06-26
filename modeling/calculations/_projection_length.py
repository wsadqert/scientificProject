from data.constants import *


def projection_length(system, fi: float):
	"""
	:type system: modeling.star.StarSystem
	"""
	if system.e == 0:
		return system.a * abs(sin(radians(fi)))
	
	return abs((system.p * sin(radians(system.periapsis_argument + fi))) / (1 + system.e * cos(radians(fi))))
