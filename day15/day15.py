from queue import PriorityQueue
with open('day15/input.txt', 'r') as f:
	matrix = [list(map(int, line)) for line in f.read().splitlines()]

def solve(m):
	h, w = len(m), len(m[0])
	pq = PriorityQueue()
	pq.put((0, (0, 0)))
	visited = {(0, 0), }
	
	while pq:
		curr_risk, (i, j) = pq.get()
		if i == h - 1 and j == w - 1:
			return curr_risk

		for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
			if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
				weight = m[x][y]
				pq.put((curr_risk + weight, (x, y)))
				visited.add((x, y))

def big(matrix):
	d = {i: j % 10 if j % 10 != 0 else 1 for i, j in zip(range(1, 10), range(2, 11))}
	big_matrix = [lst.copy() for lst in matrix]
	for _ in range(4):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				big_matrix[i].append(d[big_matrix[i][j + len(matrix) * _]])

	for _ in range(4):
		for i in range(len(matrix)):
			new_list = list()

			for j in range(len(big_matrix[0])):
				new_list.append(d[big_matrix[i + len(matrix) * _][j]])

			big_matrix.append(new_list)
	
	return big_matrix

result_1 = solve(matrix)
result_2 = solve(big(matrix))

print(f"Result 1: {result_1}\nResult 2: {result_2}")
