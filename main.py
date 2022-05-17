import numpy as np
import matplotlib.pyplot as plt
import configparser

from data.star import Star

from math import pi, log
from astropy.constants import sigma_sb, L_sun
from data.constants import *

data = configparser.ConfigParser()
data.read('./data/data.inf')


star_1 = Star(int(data['Star 1']['radius']), int(data['Star 1']['temperature']))
star_2 = Star(int(data['Star 2']['radius']), int(data['Star 2']['temperature']))
