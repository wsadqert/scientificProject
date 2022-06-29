import colorama
import matplotlib
from astropy.constants.codata2018 import G, sigma_sb
from astropy.constants.iau2015 import L_sun
from math import pi, sqrt, sin, cos, tan, acos, atan, degrees, radians, log10
from typing import Final, Sequence, Iterable

L_sun = L_sun.to_value()
G = G.to_value()
sigma_sb = sigma_sb.to_value()

abs_magnitude_sun: Final[float] = 4.75

BLACK = colorama.Fore.BLACK
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
BLUE = colorama.Fore.BLUE
MAGENTA = colorama.Fore.MAGENTA
CYAN = colorama.Fore.CYAN
WHITE = colorama.Fore.WHITE
LIGHTGREEN_EX = colorama.Fore.LIGHTGREEN_EX
RESET = colorama.Fore.RESET + '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

mpl_colors = [i['color'] for i in matplotlib.rcParams['axes.prop_cycle']]

subplot_titles: Final[tuple[str, ...]] = ('Кривая блеска (абсолютной звёздной величины)',
                                          'Кривая расстояния между центрами',
                                          '',
                                          'Кривая истинной аномалии')
subplot_labels: Final[tuple[str, ...]] = (r'$M_{abs}(t)$',
                                          r'расстояние между центрами в проекции на плоскость, перпендикулярную лучу зрения',
                                          r'расстояние между центрами',
                                          r'$\varphi(t)$')
stars_intersect_error: Final[str] = f'{RED}ERROR!{RESET} Wrong input data, modeling not possible! In the periastron, the stars intersect or approach each other at a distance less than the sum of the radii of the stars! Ways to fix the error: \n - bring the orbit closer to a circular one by reducing the eccentricity \n - increase the semi-major axis of the orbit \n - reduce the radii of stars'
not_variable_warning: Final[str] = f'{YELLOW}Warning!{RESET} Star system is not variable'
