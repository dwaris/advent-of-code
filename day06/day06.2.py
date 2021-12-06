#!/usr/bin/env python3
import numpy as np

result = 0

lines = np.loadtxt('day06/input.txt',dtype=int,delimiter=",")

counter = [np.count_nonzero(lines == i) for i in range(0, 9)]

for _ in range(256):
	counter = counter[1:] + counter[:1]
	counter[6] += counter[8]

result = sum(counter)

print(f"Result: {result}")
