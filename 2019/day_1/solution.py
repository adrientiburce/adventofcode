import os
import time
import math

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    lines = []
    for l in input.read().splitlines():
        lines.append(int(l))
    return lines


lines = parse_input("input")


def get_mass(n):
    return math.floor(n/3) - 2


def get_mass_2(n):
    fuel_total, fuel = 0, n
    while fuel > 0:
        fuel = math.floor(fuel/3) - 2
        fuel_total += fuel
    return fuel_total - fuel


def part_1(lines=lines):
    total = 0
    for n in lines:
        total += get_mass(n)
    return total


def part_2(lines=lines):
    total = 0
    for n in lines:
        total += get_mass_2(n)
    return total


def test_demo():
    assert get_mass(1969) == 654
    assert get_mass_2(1969) == 966


start = time.time()
print("Part 1:", part_1(), "/ Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start))
