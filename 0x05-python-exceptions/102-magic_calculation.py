#!/usr/bin/python3

def magic_calculation(a, b):
	result = 0
	for q in range(1, 3):
		try:
			if q > a:
				raise Exception('Too far')

			result += (a ** b) / q
		except Exception:
			result = a + b

	return result
