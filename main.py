import configparser
from typing import Final

from modeling.star import Star, StarSystem

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters_star: Final[tuple[str, ...]] = tuple(data['Star 1'].keys())
parameters_system: Final[tuple[str, ...]] = tuple(data['System'].keys())

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters_star])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters_star])

system: StarSystem = StarSystem(star1, star2, *[float(data['System'][i]) for i in parameters_system])

for fi in range(360):
	A: float = system.Period
	pass
	
print(system.calculate_transit(star1, star2), system.abs_magnitude)
print(system.calculate_touch(star1, star2, star1.radius - 0.5 * star2.radius))
