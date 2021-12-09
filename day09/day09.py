import numpy as np

lines = np.loadtxt('day09/input.txt',dtype=str)
lines = [[int(x) for x in list(line.strip())] for line in lines]

low_points = []
locations = []

VEC = [(-1,0), (0,1), (0,-1), (1,0)]

for x in range(len(lines[0])):
	for y in range(len(lines)):
		is_lowest = True
		point = lines[x][y]

		for dir in VEC:
			dx, dy = dir
		
			if y+dy in range(len(lines)) and x+dx in range(len(lines[0])):
				neighbour = lines[x+dx][y+dy]
				if neighbour <= point:
					is_lowest = False
					break
		
		if is_lowest:
			low_points.append(point+1)
			locations.append([x,y])

basins = []

for start in locations:
	visited = []
	to_visit = [start]

	while len(to_visit) > 0:
		current_point = to_visit.pop(0)
		x, y = current_point
		current_point_value = lines[x][y]

		for dir in VEC:
			dx, dy = dir
		
			if y+dy in range(len(lines)) and x+dx in range(len(lines[0])):
				neighbour = lines[x+dx][y+dy]
		
				if neighbour < 9 and neighbour >= current_point_value:
					neighbour_point = [x+dx,y+dy]

					if current_point not in visited:
						to_visit.append(neighbour_point)
		
		if current_point not in visited:
			visited.append(current_point)

	basins.append(len(visited))

result_1 = np.sum(low_points)
result_2 = np.prod(sorted(basins)[-3:])

print(f"Result 1: {result_1}\nResult 2: {result_2}")
