from astropy.constants.codata2018 import G, sigma_sb
from astropy.constants.iau2015 import L_sun
from math import pi, sqrt, sin, cos, tan, acos, atan, degrees, radians, log10
from typing import Sequence

L_sun = L_sun.to_value()
G = G.to_value()
sigma_sb = sigma_sb.to_value()

abs_magnitude_sun: float = 4.75
