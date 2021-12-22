import numpy as np
import re
from collections import Counter

lines = []
for line in open('day22/input.txt'):
	r = re.match(r"(on|off) x=(-*\d+)..(-*\d+),y=(-*\d+)..(-*\d+),z=(-*\d+)..(-*\d+)", line)
	on_off = r.groups()[0] == "on"
	x1, x2, y1, y2, z1, z2 = map(int, r.groups()[1:])
	lines.append((on_off, (x1, x2), (y1, y2), (z1, z2)))


def populate_grid():
	cubes = np.zeros((100, 100, 100), dtype=bool)
	for on_off, x, y, z in lines:
		cubes[x[0] + 50 : x[1] + 50 + 1, y[0] + 50 : y[1] + 50 + 1, z[0] + 50 : z[1] + 50 + 1] = on_off
	return cubes


def process_all_cubes():
	cubes = Counter()
	for on_off, x_next, y_next, z_next in lines:
		for (x, y, z), val in cubes.copy().items():
			ix = max(x[0], x_next[0]), min(x[1], x_next[1])
			iy = max(y[0], y_next[0]), min(y[1], y_next[1])
			iz = max(z[0], z_next[0]), min(z[1], z_next[1])

			if val == 0:
				cubes.pop((x, y, z))
				continue
			elif (
				on_off
				and val > 0
				and x_next[0] >= x[0]
				and x_next[1] <= x[1]
				and y_next[0] >= y[0]
				and y_next[1] <= y[1]
				and z_next[0] >= z[0]
				and z_next[1] <= z[1]
			):
				break
			elif (
				on_off
				and x[0] >= x_next[0]
				and x[1] <= x_next[1]
				and y[0] >= y_next[0]
				and y[1] <= y_next[1]
				and z[0] >= z_next[0]
				and z[1] <= z_next[1]
			):
				cubes[(x, y, z)] -= val

			elif ix[0] <= ix[1] and iy[0] <= iy[1] and iz[0] <= iz[1]:
				cubes[ix, iy, iz] -= val
		else:
			if on_off:
				cubes[x_next, y_next, z_next] += 1

	return cubes


def count_lights(cubes):
	return sum((x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1) * val for (x, y, z), val in cubes.items())


result_1 = populate_grid().sum()

cubes = process_all_cubes()

result_2 = count_lights(cubes)

print(f"Result 1: {result_1}\nResult 2: {result_2}")
