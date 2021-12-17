MINX, MAXX = 207, 263
MINY, MAXY = -115, -63

a = 0
b = MAXX + 1

x_positions = []
for initx in range(0, b):
	x = 0
	x_positions.append([0] + [x := x + dx for dx in range(initx, 0, -1)])

highest = -1
velocities = set()
for inity in range(MINY, -MINY):
	posy = 0
	dy = inity
	topy = 0
	n = 0
	while posy >= MINY:
		if posy <= MAXY:
			for initx in range(a, b):
				step = min(n, len(x_positions[initx]) - 1)
				
				if MINX <= x_positions[initx][step] <= MAXX:
					highest = max(highest, topy)
					velocities.add((initx, inity))
		posy += dy
		if dy == 0:
			topy = posy
		dy -= 1
		n += 1

result_1 = highest
result_2 = len(velocities)

print(f"Result 1: {result_1}\nResult 2: {result_2}")
