import configparser
from time import time
from typing import Final

import numpy as np
from matplotlib import pyplot as plt, rcParams
from rich.traceback import install
from tqdm import tqdm

from modeling.star import Star, StarSystem
from modeling.time2phi import circular_orbit

install(show_locals=True, width=300)

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters_star: Final[tuple[str, ...]] = tuple(data['Star 1'].keys())
parameters_system: Final[tuple[str, ...]] = tuple(data['System'].keys())

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters_star])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters_star])

system: StarSystem = StarSystem(star1, star2, *[float(data['System'][i]) for i in parameters_system], parameters_system)

dt: float = float(data['General']['dt'])
mags: list[float] = []
fi: float = -30
r: float = system.p


def normalize_angle(angle: float):
	while not (0 <= angle < 360):
		if angle > 360:
			angle -= 360
		if angle < 0:
			angle += 360
	return angle


t0 = time()

periods = np.arange(-1 / 12 * system.period, 13 / 12 * system.period, dt)

# x_axis_data = np.linspace(-30, 390, 420 * 1000, endpoint=True)
x_axis_data = []

for t in tqdm(periods):
# for fi in tqdm(x_axis_data):
	assert system.e == 0  # while in development
	fi = circular_orbit(t, system.period)
	x: float = system.a * abs(sin(radians(fi)))
	
	if 0 <= normalize_angle(fi) <= 90 or 270 <= normalize_angle(fi) <= 360:
		star_front, star_back = star2, star1
	else:
		star_front, star_back = star1, star2
	
	result = system.calculate_touch(star_front, star_back, x)

	x_axis_data.append(fi)
	mags.append(result['magnitude'])

t1 = time()
print(t1 - t0)
# print(system.calculate_transit(star1, star2), system.abs_magnitude)
# print(system.calculate_touch(star1, star2, star1.radius - 0.5 * star2.radius))

rcParams['mathtext.fontset'] = 'cm'
plt.grid(True, ls='--')

plt.title('Кривая блеска двойной звёздной системы')

plt.xlabel(r'$\varphi$')
plt.xticks([i for i in range(-30, 390, 30)] + [390])

plt.ylabel(r'$M_{abs}$')
plt.gca().invert_yaxis()

plt.plot(x_axis_data, mags)
# plt.plot(np.arange(-1 / 12 * system.period, 13 / 12 * system.period, dt), mags)

plt.show()
