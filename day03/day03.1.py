#!/usr/bin/env python3
from numpy import loadtxt

result = 0

lines = loadtxt('day03/input.txt',dtype=str)

gamma = ''
epsilon = ''

for i in range(len(lines[0])):
	one = 0
	zero = 0
	
	for line in lines:
		if line[i] == '1':
			one += 1
		else: 
			zero += 1
	
	if one > zero:
		gamma += '1'
		epsilon += '0'
	else:
		gamma += '0'
		epsilon += '1'

result = int(gamma,2) * int(epsilon,2)

print(f"Result: {result}")
