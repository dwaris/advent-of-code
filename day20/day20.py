import numpy as np
from scipy import ndimage
from rich.progress import track

CHARS = {
	'#': 1,
	'.': 0,
}

image = []
with open('day20/input.txt') as f:
	algorithm = list(map(CHARS.get, next(f).strip()))
	next(f)
	for line in f:
		image.append(list(map(CHARS.get, line.strip())))
image, algorithm = np.array(image), algorithm


def lookup(values):
	string = ''.join(str(int(value)) for value in values)
	return algorithm[int(string, 2)]

def apply_enhance(times):
	newimage = np.pad(image, times*2)

	for i in track(range(times)):
		newimage = ndimage.generic_filter(newimage, lookup, size=3, mode='constant', cval=0)

	return newimage[times:-times, times:-times]

newimage = apply_enhance(2)
result_1 = newimage.sum()

newimage = apply_enhance(50)
result_2 = newimage.sum()

print(f"Result 1: {result_1}\nResult 2: {result_2}")
