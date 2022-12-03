with open('input.txt') as f:
    data = f.read().splitlines()

mapped_items = {}
result = []

for i, char in enumerate(range(ord('a'), ord('z') + 1), start=1):
	mapped_items[chr(char)] = i
for i, char in enumerate(range(ord('A'), ord('Z') + 1), start=27):
	mapped_items[chr(char)] = i

for line in data:
	backback_1 = set(line[:len(line)//2])
	backback_2 = set(line[len(line)//2:])

	for item in backback_1 & backback_2:
		result.append(mapped_items[item])

result = sum(result)

print(f"Result: {result}")
