from data.constants import *


def apparent_distance(system, fi: float) -> float:
	"""
	The distance between the centers of stars in the projection onto a plane perpendicular to the line of sight
	:type system: modeling.star.StarSystem
	"""
	if system.e == 0:
		return system.a * abs(sin(radians(fi)))
	
	return abs((system.p * sin(radians(system.periapsis_argument + fi))) / (1 + system.e * cos(radians(fi))))
