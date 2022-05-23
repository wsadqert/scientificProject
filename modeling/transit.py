from .star import Star


def calculate_transit(star_front: Star, star_back: Star) -> float:
	"""Calculates absolute magnitude of star system at transit time"""
	
	if star_front.radius > star_back.radius:
		return star_front.abs_magnitude
	
	pass
