import configparser
from math import radians, sin
from typing import Final

import numpy as np
from matplotlib import pyplot as plt, rcParams
from rich.traceback import install
from tqdm import tqdm

from modeling.star import Star, StarSystem

install(show_locals=True, width=300)

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters_star: Final[tuple[str, ...]] = tuple(data['Star 1'].keys())
parameters_system: Final[tuple[str, ...]] = tuple(data['System'].keys())

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters_star])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters_star])

system: StarSystem = StarSystem(star1, star2, *[float(data['System'][i]) for i in parameters_system], parameters_system)
mags = []

for fi in tqdm(np.linspace(0, 360, 360*1000)):
	x: float = system.a * abs(sin(radians(fi)))
	qwerty = system.calculate_touch(star2, star1, x)
	# print(fi)
	mags.append(qwerty['magnitude'])

# print(system.calculate_transit(star1, star2), system.abs_magnitude)
# print(system.calculate_touch(star1, star2, star1.radius - 0.5 * star2.radius))

rcParams['mathtext.fontset'] = 'cm'
plt.grid(True, ls='--')
plt.title('Кривая блеска двойной звёздной системы')
plt.xlabel(r'$\varphi$')
plt.ylabel(r'$M_{abs}$')
plt.gca().invert_yaxis()
plt.plot(np.linspace(0, 360, 360*1000), mags)
plt.show()
