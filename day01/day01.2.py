#!/usr/bin/env python3
from numpy import loadtxt

result = 0

lines = loadtxt('day01/input.txt', dtype='int')

last = []
last_sum = -1

for line in lines:
	last.append(line)
	
	if len (last) > 3:
		last = last[1:]


	if len(last) == 3:
		line_sum = sum(last)
	else:
		line_sum = -1

	if last_sum != -1 and line_sum > last_sum:
		result += 1
	
	last_sum = line_sum

print(f"Result: {result}")
