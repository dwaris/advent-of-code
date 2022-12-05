#!/usr/bin/env python3
with open('input.txt', 'r') as f:
	data = f.read().splitlines()

stacks = [[] for _ in range(9)]

split = 0
for i in range(len(data)):
	if data[i] == '':
		split = i

for line in reversed(data[:split-1]):
	j = -1
	for i in range(1, len(line), 4):
		j += 1
		if line[i].isupper():
			stacks[j].append(line[i])

for line in data[split+1:]:
	c, x_from, x_to = [int(x) for x in line.split() if x.isnumeric()]

	x_from -= 1
	x_to -= 1

	moved = stacks[x_from][-c:]
	stacks[x_from] = stacks[x_from][:-c]
	stacks[x_to].extend(reversed(moved))

result = ""
for stack in stacks:
	if stack != []:
		result += str(stack[-1:][0])

print(f"Result: {result}")
