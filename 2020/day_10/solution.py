import os
import sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    numbers = list(map(int, input.read().splitlines()))
    numbers.sort()
    numbers = [0] + numbers  # charging outlet
    numbers = numbers + [max(numbers) + 3]  # device adapter
    return numbers


numbers = parse_input("input")


def part_1(numbers=numbers):
    diff_1 = diff_3 = 0
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == 1:
            diff_1 += 1
        elif numbers[i+1] - numbers[i] == 3:
            diff_3 += 1

    return diff_1*diff_3


def part_2(numbers=numbers):
    arrangements = [0] * len(numbers)
    arrangements[-1] = 1
    for i in range(len(numbers)-2, -1, -1):
        total = 0
        for j in range(i+1, len(numbers)):
            if numbers[j] - numbers[i] <= 3:
                total += arrangements[j]
            else:
                break
        arrangements[i] = total
    return arrangements[0]


def test_with_demo():
    assert part_1(parse_input("demo")) == 5*7
    assert part_2(parse_input("demo")) == 8


start_time = time.time()
print("\n Part 1:", part_1(), "; Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start_time))
