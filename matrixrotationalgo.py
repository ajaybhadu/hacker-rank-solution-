from math import *
from collections import deque

def rotate(listOfnumbers, count):
	leftpart = listOfnumbers[:count]
	rightpart = listOfnumbers[count:]
	return rightpart+leftpart

def printMatrix(matrix):
	for x in range(rows):
		for y in range(cols):
			print(matrix[x][y], end = ' ')
		print()

rows, cols, R = [int(x) for x in input().split()]
numberOfLayers = int(min(rows, cols)/2)
matrix = []
for x in range(rows):
	matrix.append([int(x) for x in input().split()])
listOfnumbers = []
for layer in range(numberOfLayers):
	listOfnumbers.append([matrix[layer][x] for x in range(layer, cols-layer)])
	listOfnumbers[layer].extend([matrix[x][cols-layer-1] for x in range(layer+1, rows-layer)])
	listOfnumbers[layer].extend([matrix[rows-layer-1][x] for x in range(cols-layer-2, layer-1, -1)])
	listOfnumbers[layer].extend([matrix[x][layer] for x in range(rows-layer-2, layer, -1)])
for layer in range(numberOfLayers):
	listOfnumbers[layer] = rotate(listOfnumbers[layer], R%len(listOfnumbers[layer]))
for layer in range(numberOfLayers):
	# listOfnumbers.append([matrix[layer][x] for x in range(layer, cols-layer)])
	listOfnumbers[layer] = deque(listOfnumbers[layer])
	for x in range(layer, cols-layer):
		matrix[layer][x] = listOfnumbers[layer].popleft()
	# listOfnumbers[layer].extend([matrix[x][cols-layer-1] for x in range(layer+1, rows-layer)])
	for x in range(layer+1, rows-layer):
		matrix[x][cols-layer-1] = listOfnumbers[layer].popleft()
	# listOfnumbers[layer].extend([matrix[rows-layer-1][x] for x in range(cols-layer-2, layer-1, -1)])
	for x in range(cols-layer-2, layer-1, -1):
		matrix[rows-layer-1][x] = listOfnumbers[layer].popleft()
	# listOfnumbers[layer].extend([matrix[x][layer] for x in range(rows-layer-2, layer, -1)])
	for x in range(rows-layer-2, layer, -1):
		matrix[x][layer] = listOfnumbers[layer].popleft()
printMatrix(matrix)
