from astropy import units as u
from data.constants import *


def meters2au(x: float | Iterable) -> float | list:
	if isinstance(x, float):
		return ((x * u.meter).to('au')).value
	
	return list(((x * u.meter).to('au')).value)
