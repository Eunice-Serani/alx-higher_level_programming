#!/usr/bin/python3
def magic_calculation(a, b):
	ret = 0
	for q in range(1, 3):
		try:
			if q > a:
				raise Exception('Too far')

			ret += (a ** b) / q
		except Exception:
			ret = a + b

	return ret
