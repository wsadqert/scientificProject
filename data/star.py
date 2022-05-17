from math import pi, log
from astropy.constants import sigma_sb, L_sun
from data.constants import *


class Star:
	def __init__(self, radius: float, temperature: float, mass: float):
		self.radius: float = radius
		self.temperature: float = temperature
		self.mass = mass
		
		self.square = pi * radius ** 2
		self.square_full = 4 * self.square
		self.L: float = self.square_full * sigma_sb.value * temperature ** 4
		self.abs_magnitude: float = abs_magnitude_sun - log(self.L / L_sun.value) / 0.4


class StarSystem:
	def __init__(self, star1: Star, star2: Star, T: float):
		self.T: float = T
		self.mass: float = star1.mass + star2.mass
		self.L = star1.L + star2.L
		
