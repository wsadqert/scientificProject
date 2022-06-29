from data.constants import *


def inclination_correction(system, fi: float) -> float:
	"""
	:type system: modeling.star.StarSystem
	"""
	# assert system.e == 0  # while in development
	
	# if system.e != 0 and system.inclination != 0:
	# 	return 0
	
	return system.a * sin(radians(system.inclination)) * cos(radians(system.ascending_node_longitude)) * cos(radians(fi))
