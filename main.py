import configparser
from typing import Final
from modeling.star import Star, StarSystem

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters: Final[tuple[str, str, str]] = ('Radius', 'Temperature', 'Mass')

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters])

T: float = float(data['System']['T'])

system: StarSystem = StarSystem(star1, star2, T)

print(system.calculate_transit(star1, star2))
