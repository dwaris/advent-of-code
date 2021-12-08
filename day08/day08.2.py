#!/usr/bin/env python3
import os.path
import numpy as np

data = np.loadtxt('day08/input.txt',dtype=str,delimiter='\t')

result = 0
for patterns, outputs in [line.split("|") for line in data]:
	line = {len(pattern): set(pattern) for pattern in patterns.split()}

	num = ''
	for output in map(set, outputs.split()):
		match len(output), len(output & line[4]), len(output & line[2]):
			case 2,_,_: num += '1'
			case 3,_,_: num += '7'
			case 4,_,_: num += '4'
			case 7,_,_: num += '8'
			case 5,2,_: num += '2'
			case 5,3,1: num += '5'
			case 5,3,2: num += '3'
			case 6,4,_: num += '9'
			case 6,3,1: num += '6'
			case 6,3,2: num += '0'
	result += int(num)

print(f"Result: {result}")