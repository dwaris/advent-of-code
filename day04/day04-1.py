#!/usr/bin/env python3
with open('input.txt', 'r') as f:
	data = [tuple(int(x) for pairs in row.split(',')
			for x in pairs.split('-')) for row in f.readlines()]

result = 0

for pair in data:
	x_start, x_end, y_start, y_end = pair

	if (x_start <= y_start and y_end <= x_end) or (y_start <= x_start and x_end <= y_end):
		result += 1

print(f"Result: {result}")
