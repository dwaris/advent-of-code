#!/usr/bin/env python3
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

A = np.array([list(map(int, line)) for line in data])


def distance(line, tree) -> int:
    d = 0
    for x in line:
        d += 1
        if x >= tree:
            break
    return d


result = 0

for x, y in np.ndindex(A.shape):
    tree = A[x, y]
    new_score = (
        distance(np.flip(A[x, :y]), tree)
        * distance(np.flip(A[:x, y]), tree)
        * distance(A[x + 1 :, y], tree)
        * distance(A[x, y + 1 :], tree)
    )
    result = max(result, new_score)

print(f"Result: {result}")
