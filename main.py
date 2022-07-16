import configparser
from time import process_time, time

from rich.traceback import install
from tqdm import tqdm

from matplotlib import pyplot as plt, rcParams
import matplotlib

from modeling.star import Star, StarSystem
from modeling.calculations import meters2au, normalize_angle, apparent_distance, time2phi, inclination_correction
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
periods: np.ndarray = np.arange(-1 / 6 * system.period, 7 / 6 * system.period, dt)
mags: list[float] = []
mags_corrections: list[float] = []
distances_visual: list[float] = []
distances: list[float] = []
fis: list[float] = []
x_axis_data: list[float] = []

# ---------CALCULATIONS---------

for t in tqdm(periods):
	fi = time2phi(t, system.period, system.e)
	ap = apparent_distance(system, fi)
	x: float = sqrt(ap**2 + inclination_correction(system, fi)**2)
	
	if 0 <= normalize_angle(fi) <= 90 or 270 <= normalize_angle(fi) <= 360:
		star_front, star_back = star2, star1
	else:
		star_front, star_back = star1, star2
	
	result: tuple[float, float] = system.calculate_touch(star_front, star_back, x)
	
	x_axis_data.append(t / system.period)
	mags.append(result[0])
	mags_corrections.append(result[1])
	distances_visual.append(x)
	distances.append(system.r(fi))
	fis.append(fi)

t2 = process_time()
t2_real = time()
print(f'PROCESSOR TIME: {t2 - t0} seconds')
print(f'REAL TIME: {t2_real - t0_real} seconds')
"""
if len(set(mags)) == 1:
	print(not_variable_warning)
"""
# -----SETTING UP MATPLOTLIB-----

rcParams['mathtext.fontset'] = 'cm'

axes: list[matplotlib.axes.Axes] = []

distances = meters2au(distances)
distances_visual = meters2au(distances_visual)

for i, y_data, color, title, label in zip(range(5), (mags, mags_corrections, distances_visual, distances, fis), mpl_colors, subplot_titles, subplot_labels):
	if i not in (1, 3):
		fig, ax = plt.subplots()
		axes.append(ax)
		
		plt.grid(True, ls='--')
		plt.title(title)
		
		plt.xticks(np.arange(-1.0, 2.0, 0.1))
		plt.xlabel('Доля периода')
	
	plt.plot(x_axis_data, y_data, color=color, label=label)
	
	if i == 3:
		plt.legend(loc='upper right')
		continue
	
	plt.legend()

axes[0].invert_yaxis()

axes[1].scatter(0, meters2au(system.q), color=mpl_colors[3])
axes[1].scatter(0.5, meters2au(system.Q), color=mpl_colors[3])
axes[1].scatter(1, meters2au(system.q), color=mpl_colors[3])
axes[1].fill_between(x_axis_data, distances_visual, facecolor='none', hatch='xx', edgecolor=mpl_colors[2], linewidth=0.0)

plt.sca(axes[2])
plt.yticks(range(-120, 480, 30))
axes[2].scatter(0, 0, color=mpl_colors[4])
axes[2].scatter(0.5, 180, color=mpl_colors[4])
axes[2].scatter(1, 360, color=mpl_colors[4])

# plt.savefig('qwertyu.png')
plt.show()
