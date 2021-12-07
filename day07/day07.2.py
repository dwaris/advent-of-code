#!/usr/bin/env python3
import numpy as np

result = 0

lines = np.loadtxt('day07/input.txt',dtype=int,delimiter=",")

def f(x): return int((x ** 2 + x) // 2)

result = np.sum([f(np.abs(np.floor(np.mean(lines)) - x)) for x in lines])

print(f"Result: {result}")
