#!/usr/bin/env python3
import numpy as np

lines = np.genfromtxt('day11/input.txt',delimiter=1)

result = 0

for _ in range(100):
	lines += 1
	flashing = np.argwhere(lines > 9)
	while len(flashing):
		for x, y in flashing:
			box = np.s_[max(0,x-1):x+2, max(0,y-1):y+2]
			lines[box] += lines[box] > 0
			lines[x,y] = 0

		flashing = np.argwhere(lines > 9)
	
	result += np.count_nonzero(lines == 0)

print(f"Result: {result}")
