with open('input.txt') as f:
    data = f.read().splitlines()

mapped_items = {}
result = []

for i, char in enumerate(range(ord('a'), ord('z') + 1), start=1):
	mapped_items[chr(char)] = i
for i, char in enumerate(range(ord('A'), ord('Z') + 1), start=27):
	mapped_items[chr(char)] = i

grouped_items = [[data[i], data[i+1], data[i+2]] for i in range(0, len(data), 3)]

for triplet in grouped_items:
	item_sets = [set(x) for x in triplet]
	result.append(sum([mapped_items[x] for x in set.intersection(*item_sets)]))

result = sum(result)

print(f"Result: {result}")
