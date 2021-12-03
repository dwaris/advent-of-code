#!/usr/bin/env python3
from numpy import loadtxt

result = 0

lines = loadtxt('day02/input.txt', dtype=[('direction', '|U1'),('distance', 'int')])

x = 0
z = 0

for line in lines:
	direction = line['direction']
	distance = line['distance']
	
	if direction == 'f':
		x += distance
	elif direction == 'd':
		z += distance
	else:
		z -= distance

result = x*z

print(f"Result: {result}")
