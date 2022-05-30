from math import log10, pi
from typing import Any

from astropy.constants.codata2018 import G, sigma_sb
from astropy.constants.iau2015 import L_sun

from data.constants import *
import modeling.transit as transit


class Star:
	def __init__(self, radius: float, temperature: float, mass: float):
		self.radius: float = radius
		self.temperature: float = temperature
		self.mass = mass
		
		self.square = pi * radius ** 2
		self.square_full = 4 * self.square
	
	@property
	def L(self) -> float:
		return self.square_full * sigma_sb.value * self.temperature ** 4
	
	@property
	def abs_magnitude(self) -> float:
		return abs_magnitude_sun - log10(self.L / L_sun.value) / 0.4


class StarSystem:
	def __init__(self, star1: Star, star2: Star, period: float, eccentricity: float, i: float):
		self.star1: Star = star1
		self.star2: Star = star2
		
		self.period: float = period
		self.e: float = eccentricity
		self.i: float = i
		
		self.mass: float = star1.mass + star2.mass
		self.L: float = star1.L + star2.L
		self.a: float = ((self.period ** 2 * G * self.mass) / (4 * pi ** 2)) ** 1 / 3
		
		self.calculate_transit = transit.calculate_transit
		self.calculate_touch = transit.calculate_touch
	
	@property
	def abs_magnitude(self) -> float:
		return -2.5 * log10(10 ** (-0.4 * self.star1.abs_magnitude) + 10 ** (-0.4 * self.star2.abs_magnitude))
	