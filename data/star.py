from math import pi, log
from astropy.constants import sigma_sb, L_sun
from data.constants import *


class Star:
	def __init__(self, radius: float, temperature: float):
		self.radius: float = radius
		self.temperature: float = temperature
		self.L: float = 4 * pi * sigma_sb.value * radius ** 2 * temperature ** 4
		self.abs_magnitude: float = abs_magnitude_sun - log(self.L / L_sun.value) / 0.4
