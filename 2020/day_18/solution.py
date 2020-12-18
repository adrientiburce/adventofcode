import os
import time
import re
from typing import Callable


dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    return input.read().splitlines()


lines = parse_input("input")


def eval1(s):
	s_list = s.split(" ")
	if len(s_list) < 3:
		return s[:-1]
	res = eval("".join(s_list[:3])) # eval first operation
	return eval1(str(res) + " " + " ".join(s_list[3:]))


def eval2(s):
	res = 1
	for additions in s.split(" * "):
		res *= sum(map(int, additions.split(" + ")))
	return str(res)


def compute(exp :str, eval_p: Callable[[str], str]) -> int:
	if "(" not in exp:
		return int(eval_p(exp))
	for match in re.finditer(r"\(([^\(\)]*)\)", exp):
		exp = exp.replace(match.group(), eval_p(match.group()[1:-1]))
	return compute(exp.replace("  ", " "), eval_p)


def part_1(lines=lines):
	return sum(map(lambda x: compute(x, eval1), lines))


def part_2(lines=lines):
	return sum(map(lambda x: compute(x, eval2), lines))


def test_demo():
    assert compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", eval1) ==  12240
    assert compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", eval2) ==  669060

start = time.time()
print("Part 1:", part_1(), "/ Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start))
