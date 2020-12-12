import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    lines = []
    for l in input.read().splitlines():
        lines.append(list(l))
    return lines


lines = parse_input("input")


def part_1(lines=lines):
    pass


def part_2(lines=lines):
    pass


def test_demo():
    pass
    # assert part_1(parse_input("demo")) ==  ## REPLATE HERE !!##
    # assert part_2(parse_input("demo")) ==  ## REPLATE HERE !!##


start = time.time()
print("Part 1:", part_1(), "/ Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start))
