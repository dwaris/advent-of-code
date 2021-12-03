#!/usr/bin/env python3
from numpy import loadtxt

result = 0

lines = loadtxt('day01/input.txt', dtype='int')

last = -1

for line in lines:
	if last != -1 and line > last:
		result += 1
	last = line

print(f"Result: {result}")
