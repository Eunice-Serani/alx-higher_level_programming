#!/usr/bin/python3
def roman_to_int(roman_string):
	if not roman_string or type(roman_string) != str:
		return 0
	total = 0
	package = 0
	roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
	for i in reversed(roman_string):
		package = roman_num[i]
		total += package if total < package * 5 else -package
	return total
