import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('day13/input.txt',dtype=int,delimiter=',',max_rows=794)
folds = np.loadtxt('day13/input.txt',dtype=str,delimiter='=',skiprows=795)
folds[:,0] = [i[-1] for i in folds[:,0]]

for axis,value in zip(folds[:,0],folds[:,1].astype(int)):
	for point in range(len(points)):
		if axis == 'x':
			if points[point][0] > value:
				new_value = points[point][0] - 2 *(points[point][0] - value)
				points[point] = np.array([new_value,points[point][1]])

		elif axis == 'y':
			if points[point][1] > value:
				new_value = points[point][1] - 2 *(points[point][1] - value)
				points[point] = np.array([points[point][0],new_value])


picture = np.zeros([6,np.max(points)+1])

for p in points:
	picture[p[1],p[0]] += 1

plt.imshow(picture > 0)
plt.show()
