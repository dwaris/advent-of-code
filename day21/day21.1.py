x = [6, 7]
y = [0, 0]
c, o, k = 0, 0, 0

while True:
	for i in range(3):
		o += 1
		k = k % 100 + 1
		x[c] = (x[c] + k - 1) % 10 + 1
	y[c] += x [c]

	if y[c] >= 1000:
		result = o*min(y)
		break
	c = (c + 1) % 2

print(f"Result: {result}")
