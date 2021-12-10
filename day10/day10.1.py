#!/usr/bin/env python3
import numpy as np

lines = np.loadtxt('day10/input.txt', dtype=str, delimiter="\t")

result = 0

OPEN = ["(", "[", "{", "<"]
CLOSE = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

SCORES = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

for line in lines:
	stack = []
	
	for char in line:
		if char in OPEN:
			stack.append(char)
		else:
			opening = stack.pop()
			if char != CLOSE[opening]:
				result += SCORES[char]
				break

print(f"Result: {result}")
