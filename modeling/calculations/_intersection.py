from data.constants import *


def calculate_intersection(R1: float, R2: float, D: float) -> float:
	R1, R2 = min(R1, R2), max(R1, R2)
	
	if D > R1 + R2:
		return 0
	
	if D < R2 - R1:
		return pi * min(R1, R2) ** 2
	
	# see `/src/intersection.gif`, `/src/intersection_solution.jpeg`
	
	def calculate_cos_theorem(r1: float, r2: float, d: float) -> float:
		return degrees(acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1)))
	
	alpha1: float = calculate_cos_theorem(R1, R2, D)
	alpha2: float = calculate_cos_theorem(R2, R1, D)
	
	S_sector_1: float = (alpha1 * pi * R1 ** 2) / 360
	S_sector_2: float = (alpha2 * pi * R2 ** 2) / 360
	
	S_triangle1: float = 1 / 2 * R1 ** 2 * cos(radians(alpha1)) * sin(radians(alpha1))
	S_triangle2: float = 1 / 2 * R2 ** 2 * cos(radians(alpha2)) * sin(radians(alpha2))
	
	A1: float = S_sector_1 - S_triangle1
	A2: float = S_sector_2 - S_triangle2
	
	return 2 * (A1 + A2)
