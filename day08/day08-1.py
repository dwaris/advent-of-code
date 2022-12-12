#!/usr/bin/env python3
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

A = np.array([list(map(int, line)) for line in data])


result = 0

for x, y in np.ndindex(A.shape):
    current_tree = A[x, y]
    if (
        all(A[x, :y] < current_tree)
        or all(A[:x, y] < current_tree)
        or all(A[x + 1 :, y] < current_tree)
        or all(A[x, y + 1 :] < current_tree)
    ):
        result += 1

print(f"Result: {result}")
