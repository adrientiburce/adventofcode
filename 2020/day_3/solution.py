import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f'{dir_path}/input.txt', 'r')
lines = input.readlines()

n = len(lines)
lenLine = len(lines[0].rstrip())


def getSlopeTrees(xSlope: int, ySlope: int) -> int:
    count = 0
    xPos = 0
    for yPos in range(ySlope, n, ySlope):
        xPos += xSlope
        char = lines[yPos][xPos % lenLine]
        count += (char == "#")
    return count


# PART ONE:
print(getSlopeTrees(3, 1))

# PART TWO:
xSlopes = [1, 3, 5, 7, 1]
ySlopes = [1, 1, 1, 1, 2]

allRes = []
for i in range(len(xSlopes)):
    res = getSlopeTrees(xSlopes[i], ySlopes[i])
    allRes.append(res)
print(allRes)
print(math.prod(allRes))
