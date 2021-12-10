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
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

total = []

for line in lines:
    stack = []
    local_score = 0

    for char in line:
        if char in OPEN:
            stack.append(char)
        else:
            opening = stack.pop()
            if char != CLOSE[opening]:
                break

    else:
        if stack:
            for opening in stack[::-1]:
                local_score *= 5
                local_score += SCORES[opening]

            total.append(local_score)

result = int(np.median(total))

print(f"Result: {result}")
