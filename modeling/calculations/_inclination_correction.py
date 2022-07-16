from data.constants import *


def inclination_correction(system, fi: float) -> float:
	"""
	:type system: modeling.star.StarSystem
	"""
	
	return system.a * sin(radians(system.inclination)) * cos(radians(system.ascending_node_longitude)) * cos(radians(fi))
