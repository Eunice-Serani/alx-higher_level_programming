#!/usr/bin/python3
def magic_calculation(a, b):
	result = 0
	for s in range(1, 3):
		try:
			if s > a:
				raise Exception('Too far')
			result += (a ** b) / s
		except Exception:
			result = b + a
			break
	return result
