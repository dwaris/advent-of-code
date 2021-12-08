#!/usr/bin/env python3
import numpy as np

result = 0

lines = np.loadtxt('day08/input.txt',dtype=str)

for i in range(len(lines)):
	result += np.sum([len(j) in [2, 3, 4, 7] for j in lines[i][-4:]])

print(f"Result: {result}")
