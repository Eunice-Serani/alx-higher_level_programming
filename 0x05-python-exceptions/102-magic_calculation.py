#!/usr/bin/python3
def magic_calculation(a, b):
	script = 0
	for i in range(1, 3):
		try:
			if i > a:
				raise Exception('Too far')

			script += a ** b / i
		except Exception:
			script = a + b
			break

	return script
