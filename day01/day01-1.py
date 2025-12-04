#!/usr/bin/env python3
with open('input.txt', 'r') as infile:
    data = [int(x) for x in infile.read().strip().replace('L', '-').replace('R', '+').split('\n')]

counter = 0
dial = 50
for move in data:
    if dial + move >= 100:
        dial = (dial + move) % 100
    elif dial + move < 0:
        dial = (dial + move + 100) % 100
    else:
        dial += move
    if dial == 0:
        counter += 1

print(f"Result: {counter}")
