with open('input.txt', 'r') as f:
	data = f.read().splitlines()[0]

result = 0
n = 14

for i in range(len(data)):

	blocks = set(data[i:i + n])

	if n == len(blocks):
		result = i + n
		break

print(f"Result: {result}")
