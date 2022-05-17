import numpy as np
import matplotlib.pyplot as plt
import configparser

from math import pi, log
from astropy.constants import sigma_sb, L_sun
from data.constants import *

data = configparser.ConfigParser()
data.read('./data/data.inf')


class Star:
	def __init__(self, radius, temperature):
		self.radius: int = radius
		self.temperature: int = temperature
		self.L: float = 4 * pi * sigma_sb * radius**2 * temperature**4
		self.abs_magnitude = abs_magnitude_sun - (log(self.L / L_sun))/0.4
	
	pass


star_1 = dict(data['Star 1'])
star_2 = dict(data['Star 2'])