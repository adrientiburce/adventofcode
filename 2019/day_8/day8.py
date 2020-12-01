import numpy as np
from PIL import Image

image = open("2019/day8.txt", "r")
layers = image.read()


def part1():
	minPerLayer = 151
	layerStartWithMin = 0
	# find layer with min 0
	i = 0
	while i < len(layers) - 150:
		pixel = i
		currentCount0 = 0
		while pixel < i + 150:
			if int(layers[pixel]) == 0:
				currentCount0 += 1
			pixel += 1
		if currentCount0 < minPerLayer:
			layerStartWithMin = i
			minPerLayer = currentCount0
		i = pixel
	print(minPerLayer, layerStartWithMin)

	n0, n1 = 0, 0
	for i in range(layerStartWithMin, layerStartWithMin + 150):
		if int(layers[i]) == 1:
			n0 += 1
		elif int(layers[i]) == 2:
			n1 += 1
	print(n0 * n1)

# part1()

print(len(layers))


data = np.zeros([6, 25, 3],dtype=np.uint8)

def part2():
	# iterate over pixel
	for i in range(150):
		# iterate over every layers and find first non transparent
		j = 0
		while j < len(layers) / 150:
			m = i + 150*j
			if int(layers[m]) == 2:
				j += 1
			else:
				p = 255 if int(layers[m]) == 1 else 0
				data[i//25, i%25] = p
				break
	img = Image.fromarray(data, 'RGB')
	img.save("./my.png")

part2()
