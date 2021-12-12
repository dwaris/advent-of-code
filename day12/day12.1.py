from collections import defaultdict

result = 0
queue = [['start']]
lines = defaultdict(list)

for line in open('day12/input.txt'):
	a, b = line.strip().split('-')
	lines[a].append(b)
	lines[b].append(a)


while queue:
	path = queue.pop(0)

	for node in lines[path[-1]]:
		if node == 'end':
			result += 1
		
		elif not (node.islower() and node in path):
			queue.append(path + [node])

print(f'Result: {result}')
