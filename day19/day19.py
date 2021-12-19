import itertools
from collections import Counter

lines = open("day19/input.txt").read().splitlines()
scanners = []
current = []

for l in lines:
	if l == "":
		continue
	
	elif l[0:3] == "---":
		current = []
		scanners.append(current)
	
	else:
		current.append(tuple(map(int, l.split(","))))

def align(aligned, guess):
	ret = []
	dl = []
	dp = dpp = None
	for dim in range(3):
		x = [pos[dim] for pos in aligned]
		for (d,s) in [(0,1),(1,1),(2,1),(0,-1),(1,-1),(2,-1)]:
			if d == dp or d == dpp:
				continue
			
			t = [pos[d]*s for pos in guess]
			w = [b-a for (a,b) in itertools.product(x, t)]
			c = Counter(w).most_common(1)
			if c[0][1] >= 12:
				break

		if c[0][1] < 12:
			return None
		
		(dpp, dp) = (dp, d)
		ret.append([v - c[0][0] for v in t])
		dl.append(c[0][0])
	return (list(zip(ret[0],ret[1],ret[2])), dl)

result = set()
next = [ scanners[0] ]
rest = scanners[1:]
SHIFTS = [(0,0,0)]
while next:
	aligned = next.pop()
	tmp = []
	for guess in rest:
		r = align(aligned, guess)
		if r:
			(updated, shift) = r
			SHIFTS.append(shift)
			next.append(updated)
		else:
			tmp.append(guess)
	rest = tmp
	result.update(aligned)

result_1 = len(result)
result_2 = max(sum(abs(a-b) for (a,b) in zip(l,r)) for l,r in itertools.product(SHIFTS,SHIFTS))

print(f"Result 1: {result_1}\nResult 2: {result_2}")
