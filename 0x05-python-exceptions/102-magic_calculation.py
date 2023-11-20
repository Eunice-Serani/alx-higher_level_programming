#!/usr/bin/python3
def magic_calculation(a, b):
	script = 0
	for q in range(1, 3):
		try:
			if q > a:
				raise Exception('Too far')

			script += (a ** b) / q
		except Exception:
			script = a + b
			break
	return script
