import os
from typing import NamedTuple
import subprocess
import time


def parse_input(file_name: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dirs = []
    lines = open(f"{dir_path}/{file_name}.txt", "r")
    for l in lines.read().splitlines():
        dirs.append((l[0], int(l[1:])))
    return dirs


class Coord(NamedTuple):
    x: int
    y: int

    def distance(self) -> int:
        return abs(self.x) + abs(self.y)


DIRECTIONS = ["E", "S", "W", "N"]


def change_direction(direction: tuple, pos: Coord) -> tuple:
    d, n = direction
    if d == "E":
        return Coord(pos.x + n, pos.y)
    elif d == "W":
        return Coord(pos.x - n, pos.y)
    elif d == "N":
        return Coord(pos.x, pos.y + n)
    elif d == "S":
        return Coord(pos.x, pos.y - n)


def part_1(directions: list):
    ship_dir = "E"
    ship_pos = Coord(0, 0)
    for direction in directions:
        d, n = direction
        if (d == "R" or d == "L"):
            i = n // 90 if d == "R" else - n // 90
            new_i = (DIRECTIONS.index(ship_dir) + i) % 4
            ship_dir = DIRECTIONS[new_i]
        else:
            if d == "F":
                direction = (ship_dir, n)
            ship_pos = change_direction(direction, ship_pos)
    return ship_pos.distance()


def rotate(d: str, way: Coord):
    if d == "R":
        return Coord(way.y, -1 * way.x)
    elif d == "L":
        return Coord(-1 * way.y, way.x)


def part_2(directions: list):
    waypoint = Coord(10, 1)
    ship_pos = Coord(0, 0)
    for direction in directions:
        d, n = direction
        if (d == "R" or d == "L"):
            for i in range(n // 90):
                waypoint = rotate(d, waypoint)
        elif d == "F":
            ship_pos = Coord(ship_pos.x + n * waypoint.x,
                             ship_pos.y + n * waypoint.y)
        else:
            waypoint = change_direction(direction, waypoint)
    return ship_pos.distance()


def test_demo():
    assert part_1(parse_input('demo')) == 25
    assert part_2(parse_input('demo')) == 286


start_time = time.time()

directions = parse_input('input')
print("Part 1:", part_1(directions), "/ Part 2:", part_2(directions))
print("--- %.4f seconds ---" % (time.time() - start_time))
