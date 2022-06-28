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

subplot_titles: Final[tuple[str, ...]] = ('Кривая блеска (абсолютной звёздной величины)',
                                          'Кривая расстояния между центрами',
                                          '',
                                          'Кривая истинной аномалии')
subplot_labels: Final[tuple[str, ...]] = (r'$M_{abs}(t)$',
                                          r'расстояние между центрами в проекции на плоскость, перпендикулярную лучу зрения',
                                          r'расстояние между центрами',
                                          r'$\varphi(t)$')
stars_intersect_error: Final[str] = 'Неправильные входные данные, моделирование невозможно! В периастре звёзды пересекаются или подходят друг к другу на расстояние, меньшее суммы радиуов звёзд! Способы устранения ошибки: \n - уменьшить эксцентриситет, приблизив орбиту к круговой \n - увеличить большую полуось орбиты \n - уменьшить радиусы звёзд'

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
