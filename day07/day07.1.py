#!/usr/bin/env python3
import numpy as np

result = 0

lines = np.loadtxt('day07/input.txt',dtype=int,delimiter=",")

result = np.sum([np.abs(int(np.median(lines)) - x) for x in lines])

print(f"Result: {result}")
