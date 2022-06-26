from data.constants import *


def interpolate(value: float, data: Sequence[Sequence[float]]) -> float:
	return data[0][1] + (value - data[0][0]) * ((data[1][1] - data[0][1]) / (data[1][0] - data[0][0]))
