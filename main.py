import configparser
from time import process_time, time
from typing import Final

import numpy as np
from matplotlib import pyplot as plt, rcParams
from rich.traceback import install
from tqdm import tqdm

from modeling.star import Star, StarSystem
from modeling.time2phi import *
from data.constants import *

t0 = process_time()
t0_real = time()

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


def normalize_angle(angle: float):
	while not (0 <= angle < 360):
		if angle > 360:
			angle -= 360
		if angle < 0:
			angle += 360
	return angle


periods: np.ndarray = np.arange(-1 / 12 * system.period, 13 / 12 * system.period, dt)

x_axis_data: list[float] = []
# times: list[float] = []

t1 = process_time()
t1_real = time()

for t in tqdm(periods):
	fi = elliptical_orbit(t, system.period, system.e) + system.periapsis_argument
	x: float = system.a * abs(sin(radians(fi)))
	
	if 0 <= normalize_angle(fi) <= 90 or 270 <= normalize_angle(fi) <= 360:
		star_front, star_back = star2, star1
	else:
		star_front, star_back = star1, star2
	
	result = system.calculate_touch(star_front, star_back, x)
	
	# times.append(t / system.period)
	x_axis_data.append(t / system.period)
	mags.append(result['magnitude'])

t2 = process_time()
t2_real = time()
print(f'PROCESSOR TIME:\n{"-" * 15}\n{t2 - t0} seconds in total\n{t2 - t1} seconds calculating\n{t1 - t0} seconds setting up ({(t1 - t0) / (t2 - t1) * 100}%)\n')
print(f'REAL TIME:\n{"-" * 15}\n{t2_real - t0_real} seconds in total\n{t2_real - t1_real} seconds calculating\n{t1_real - t0_real} seconds setting up ({(t1_real - t0_real) / (t2_real - t1_real) * 100}%)')

rcParams['mathtext.fontset'] = 'cm'
plt.grid(True, ls='--')

plt.title('Кривая блеска двойной звёздной системы')

plt.xlabel(r'$\varphi$')
# plt.xticks(range(-30, 390, 30) + [390])  #
plt.xticks(np.arange(0.0, 1.1, 0.1))
plt.xlim(-0.1, 1.1)

plt.ylabel(r'$M_{abs}$')
plt.gca().invert_yaxis()

plt.plot(x_axis_data, mags)
# plt.plot(times, x_axis_data)

plt.show()
