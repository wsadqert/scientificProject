import configparser
from typing import Final
from modeling.star import Star, StarSystem

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters_star: Final[tuple[str, str, str]] = ('Radius', 'Temperature', 'Mass')
parameters_system: Final[tuple[str, str, str]] = ('Period', 'Eccentricity', 'i')

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters_star])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters_star])

system: StarSystem = StarSystem(star1, star2, *[float(data['System'][i]) for i in parameters_system])

print(system.calculate_transit(star1, star2), system.abs_magnitude)
