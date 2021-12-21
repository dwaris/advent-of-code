from functools import cache

x, y = 6, 7

@cache
def d(x, y, a=0, b=0):
	if y >= 21:
		return [1, 0]
	if b >= 21:
		return [0, 1]
	
	w = [0, 0]

	for i in range(1, 4):
		for ii in range(1, 4):
			for iii in range(1, 4):
				xx = (x+i+ii+iii-1) % 10 + 1
				xa = a + xx
				u = d(y, xx, b, xa)
				w = [w[0] + u[1], w[1] + u[0]]
	return w

result = max(d(x, y))

print(f"Result: {result}")
