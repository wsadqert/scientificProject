import sys
import modeling.transit as transit
from data.constants import *


def abs_magnitude(L: float) -> float:
	return abs_magnitude_sun - log10(L / L_sun) * 100**0.2


class Star:
	def __init__(self, radius: float, temperature: float, mass: float):
		self.radius: float = radius
		self.temperature: float = temperature
		self.mass: float = mass
		
		self.square: float = pi * radius ** 2
		self.square_full: float = 4 * self.square
		
		self.abs_magnitude = abs_magnitude(self.L)
	
	@property
	def L(self) -> float:
		return self.square_full * sigma_sb * self.temperature ** 4
	

class StarSystem:
	def __init__(self, star1: Star, star2: Star, value: float, eccentricity: float, inclination: float, periapsis_argument: float, ascending_node_longitude: float, params: tuple[str, ...]):
		"""
		:param value: semi-major axis OR period
		"""
		self.star1: Star = star1
		self.star2: Star = star2
		
		self.mass: float = star1.mass + star2.mass
		self.L: float = star1.L + star2.L
		
		if 'period' in params:
			self.period: float = value
			self.a: float = ((self.period ** 2 * G * self.mass) / (4 * pi ** 2)) ** (1 / 3)
		elif 'semi-major_axis' in params:
			self.a: float = value
			self.period: float = sqrt((4 * pi**2 * self.a**3) / (G * self.mass))
		else:
			from ctypes import ArgumentError
			raise ArgumentError("not enough parameters")

		self.e: float = eccentricity
		self.inclination: float = inclination
		self.periapsis_argument: float = periapsis_argument
		self.ascending_node_longitude: float = ascending_node_longitude
		
		self.q: float = self.a * (1 - self.e)
		self.Q: float = self.a * (1 + self.e)
		self.p: float = self.a * (1 - self.e**2)
		
		assert 0 <= self.e < 1
		
		if self.q < (star1.radius + star2.radius):
			# stars intersect in periapsis - incorrect!
			print(RED, stars_intersect_error, RESET, sep='')
			sys.exit(1)
	
	def __contains__(self, star: Star):
		return star in (self.star1, self.star2)
	
	
	def calculate_transit(self, star1: Star, star2: Star) -> float:
		return transit.calculate_transit(self, star1, star2)
	
	def calculate_touch(self, star1: Star, star2: Star, x: float) -> tuple[float, float]:
		return transit.calculate_touch(self, star1, star2, x)

	@property
	def abs_magnitude(self) -> float:
		return -2.5 * log10(10 ** (-0.4 * self.star1.abs_magnitude) + 10 ** (-0.4 * self.star2.abs_magnitude))
	
	def r(self, fi):
		return abs(self.p / (1 + self.e * cos(radians(fi))))
	