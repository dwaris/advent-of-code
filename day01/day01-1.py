#!/usr/bin/env python3
with open('input.txt', 'r') as infile:
    data = [sum([int(c) for c in x.split('\n')]) for x in infile.read()[:-1].split('\n\n')]

result = max(data)

print(f"Result: {result}")
