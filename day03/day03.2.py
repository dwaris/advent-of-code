#!/usr/bin/env python3
from numpy import loadtxt

result = 0

lineA = loadtxt('day03/input.txt',dtype=str)
lineB = lineA
for i in range(len(lineA[0])):
	if len(lineA) != 1:
		one = []
		zero = []
		
		for line in lineA:
			if line[i] == '1':
				one += [line]
			else: 
				zero += [line]
		
		if len(one) >= len(zero):
			lineA = one
		else:
			lineA = zero
	life = int(lineA[0],2)

	if len(lineB) != 1:		
		one = []
		zero = []
		
		for line in lineB:
			if line[i] == '1':
				one += [line]
			else: 
				zero += [line]
			if len(one) < len(zero):
				lineB = one
			else:
				lineB = zero

	oxygen = int(lineB[0],2)

result = life * oxygen

print(f"Result: {result}")
