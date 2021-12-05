#!/usr/bin/env python3
import numpy as np

result = 0

lines = np.fromregex('day05/input.txt', r'[0-9]+', [("num", np.int16)]).reshape(-1,2,2)['num']
matrix = np.zeros((np.max(lines)+1,np.max(lines)+1), dtype=int)

for (x1, y1), (x2, y2) in lines:
	if x1 == x2:
		y1, y2 = min(y1, y2), max(y1, y2)
	
		for y in range(y1, y2 + 1):
			matrix[x1,y] += 1
	
	elif y1 == y2:
		x1, x2 = min(x1, x2), max(x1, x2)
		
		for x in range(x1, x2 + 1):
			matrix[x,y1] += 1

	else:
		dirX = dirY = 1
		if x2 < x1:
			dirX = -1
		if y2 < y1:
			dirY = -1
		for i in range(abs(x1 - x2) + 1):
			matrix[x1 + i * dirX, y1 + i * dirY] += 1
			
result = np.count_nonzero(matrix > 1)
print(f"Result: {result}")
