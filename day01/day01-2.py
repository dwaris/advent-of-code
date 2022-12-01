#!/usr/bin/env python3
with open('input.txt', 'r') as infile:
    data = sorted([sum([int(c) for c in x.split('\n')]) for x in infile.read()[:-1].split('\n\n')])

result = sum(data[-3:])

print(f"Result: {result}")
