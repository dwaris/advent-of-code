from collections import defaultdict

with open("input.txt") as f:
	data = f.readlines()

sizes = defaultdict(int)
paths = []

for line in data:
	match line.split():
		case '$', 'cd', '..': paths.pop()
		case '$', 'cd', dir:
			tmp = '/'
			if dir != '/':
				tmp += dir
			paths.append('/'.join(paths) + tmp)
		case size, _ if size.isdigit() :
			for dir in paths:
				sizes[dir] += int(size)

result = min(size for size in sizes.values() if size >= sizes['/'] - 40_000_000)

print(f"Result: {result}")
