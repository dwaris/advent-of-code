from collections import defaultdict

with open('input.txt') as f:
    data = f.read().splitlines()

mapped_items = {}
result = []

for i, char in enumerate(range(ord('a'), ord('z') + 1), start=1):
	mapped_items[chr(char)] = i
for i, char in enumerate(range(ord('A'), ord('Z') + 1), start=27):
	mapped_items[chr(char)] = i


grouped_items = defaultdict(list)

group_num = 0
for i, line in enumerate(data):
	if not i % 3:
		group_num += 1

	grouped_items[group_num].append(line)

for triplet in grouped_items.values():
	item_sets = [set(x) for x in triplet]
	result.append(sum([mapped_items[x] for x in set.intersection(*item_sets)]))

result = sum(result)

print(f"Result: {result}")
