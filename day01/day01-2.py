#!/usr/bin/env python3
with open('input.txt', 'r') as infile:
    data = [int(x) for x in infile.read().strip().replace('L', '-').replace('R', '+').split('\n')]

counter = 0
dial = 50
for move in data:
    m_abs = abs(move)
    if m_abs > 0:
        if move > 0:
            needed = (100 - dial) % 100
        else:
            needed = dial % 100
        if needed == 0:
            needed = 100 

        if m_abs >= needed:
            adds = (m_abs - needed) // 100 + 1
            counter += adds

    dial = (dial + move) % 100

print(f"Result: {counter}")
