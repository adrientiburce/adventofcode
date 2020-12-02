import os


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f'{dir_path}/input.txt', 'r')
lines = []
for line in input.readlines():
    lines.append(line.rstrip().split(","))


def fillRight(posStart: Point, size: int, wire):
    for i in range(posStart.x + 1, posStart.x + size + 1):
        wire.append(Point(i, posStart.y))


def fillLeft(posStart: Point, size: int, wire: list):
    for i in range(posStart.x - 1, posStart.x - size - 1, -1):
        wire.append(Point(i, posStart.y))


def fillUp(posStart: Point, size: int, wire: list):
    for i in range(posStart.y + 1, posStart.y + size + 1, 1):
        wire.append(Point(posStart.x, i))


def fillDown(posStart: Point, size: int, wire: list):
    for i in range(posStart.y - 1, posStart.y - size - 1, -1):
        wire.append(Point(posStart.x, i))


wires = []  # contains each wire's successive position
i = 0
for line in lines:
    startPosition = Point(0, 0)
    wires.append([startPosition])
    wire = wires[i]
    for instruction in line:
        size = int(instruction[1:])
        direction = instruction[:1]
        if direction == "R":
            fillRight(startPosition, size, wire)
        elif direction == "L":
            fillLeft(startPosition, size, wire)
        elif direction == "U":
            fillUp(startPosition, size, wire)
        elif direction == "D":
            fillDown(startPosition, size, wire)
        startPosition = wire[-1]
    i += 1

common = list(set(wires[0]).intersection(wires[1]))[1:]

# ======== PART ONE ==========


def getDistance(point: Point):
    return abs(point.y) + abs(point.x)


distances = map(getDistance, common)
print(min(distances))

# ======== PART TWO ==========


def getSumDistance(point: Point):
    """my comment
    """
    return wires[0].index(point) + wires[1].index(point)


distancesSumWires = map(getSumDistance, common)
print(min(distancesSumWires))
