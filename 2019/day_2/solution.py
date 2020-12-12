import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    lines = list(map(int, input.read().split(",")))
    return lines


lines = parse_input("input")


def read_opcode(l: list):
    i = 0
    while i < len(l):
        if l[i] == 99:
            break
        v_1, v_2, v_3, v_4 = l[i:i+4]
        # one block
        res = l[v_2] + l[v_3] if v_1 == 1 else l[v_2] * l[v_3]
        if v_4 < len(l):
            l[v_4] = res
        else:
            return l
        i += 4
    return l


def part_1(l=lines):
    nums = l[:]
    nums[1], nums[2] = 12, 2
    return read_opcode(nums)[0]


def part_2(optcodes=lines):
    for i in range(100):
        for j in range(100):
            l = optcodes[:]
            l[1], l[2] = i, j
            res = read_opcode(l)[0]
            if res == 19690720:
                return 100 * i + j


def test_demo():
    assert read_opcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
        30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert read_opcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


start = time.time()
print("Part 1:", part_1(), "/ Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start))
