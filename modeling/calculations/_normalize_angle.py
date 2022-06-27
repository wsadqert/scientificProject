def normalize_angle(angle: float):
	while not (0 <= angle < 360):
		if angle > 360:
			angle -= 360
		if angle < 0:
			angle += 360
	return angle
