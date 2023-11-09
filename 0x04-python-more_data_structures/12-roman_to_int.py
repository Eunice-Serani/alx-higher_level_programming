#!/usr/bin/python3
def roman_to_int(roman_string):
	if not roman_string or type(roman_string) != str:
		return 0
	total = 0
	package = 0
	roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	for i in reversed(roman_string):
		package = roman_num[i]
		total += package if total < package * 5 else -package
	return total
