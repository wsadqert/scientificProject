import configparser
from time import process_time, time
from typing import Final

import numpy as np
from matplotlib import pyplot as plt, rcParams
from rich.traceback import install
from tqdm import tqdm

from modeling.star import Star, StarSystem
from modeling.calculations import projection_length, time2phi
from data.constants import *

t0 = process_time()
t0_real = time()

# Setting up

install(show_locals=True, width=300)

data = configparser.ConfigParser()
data.read('./data/data.ini')

parameters_star: Final[tuple[str, ...]] = tuple(data['Star 1'].keys())
parameters_system: Final[tuple[str, ...]] = tuple(data['System'].keys())

star1: Star = Star(*[float(data['Star 1'][i]) for i in parameters_star])
star2: Star = Star(*[float(data['Star 2'][i]) for i in parameters_star])

system: StarSystem = StarSystem(star1, star2, *[float(data['System'][i]) for i in parameters_system], parameters_system)

dt: Final[float] = float(data['General']['dt'])
periods: np.ndarray = np.arange(-1 / 12 * system.period, 13 / 12 * system.period, dt)
mags: list[float] = []
distances_visual: list[float] = []
distances: list[float] = []
fis: list[float] = []
x_axis_data: list[float] = []

# Calculations

for t in tqdm(periods):
	fi = time2phi(t, system.period, system.e)
	x: float = projection_length(system, fi)
	
	if 0 <= normalize_angle(fi) <= 90 or 270 <= normalize_angle(fi) <= 360:
		star_front, star_back = star2, star1
	else:
		star_front, star_back = star1, star2
	
	result = system.calculate_touch(star_front, star_back, x)
	
	x_axis_data.append(t / system.period)
	
	mags.append(result)
	distances_visual.append(x)
	distances.append(abs(system.p / (1 + system.e * cos(radians(fi)))))
	fis.append(fi)

t2 = process_time()
t2_real = time()
print(f'PROCESSOR TIME: {t2 - t0} seconds')
print(f'REAL TIME: {t2_real - t0_real} seconds')

# Setting up matplotlib

fig, axes = plt.subplots(2, 2)
ax1, ax2, ax3, ax4 = axes.flat

plt.setp(axes, xlabel='Доля периода', xticks=np.arange(0.0, 1.1, 0.1), xlim=(-0.1, 1.1))

for ax in axes.flat:
	ax.grid(True, ls='--')

ax1.set_title('Кривая блеска (абсолютной звёздной величины)')
ax2.set_title('Кривая расстояния в проекции на плоскость, перпендикулярную лучу зрения')
ax3.set_title('Кривая расстояния между центрами')
ax4.set_title('Кривая истинной аномалии')

ax1.invert_yaxis()

ax1.plot(x_axis_data, mags)
ax2.plot(x_axis_data, distances_visual)
ax3.plot(x_axis_data, distances)
ax4.plot(x_axis_data, fis)

plt.show()
