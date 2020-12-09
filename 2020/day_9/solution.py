import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
numbers = list(map(int, input.read().splitlines()))

PREAMBLE = 25
n = len(numbers)


def find_sum(i_num: int) -> bool:
    for i in range(i_num-PREAMBLE, n):
        for j in range(i_num-PREAMBLE+1, n):
            if numbers[i] + numbers[j] == numbers[i_num]:
                return True
    return False


def part1() -> int:
    for i in range(PREAMBLE, n):
        if not find_sum(i):
            return numbers[i]


def part2(res: int) -> list:
    for i in range(0, n):
        current_sum = numbers[i]
        next_i = i + 1
        while current_sum < res and next_i < n:
            current_sum += numbers[next_i]
            next_i += 1
        if current_sum == res:
            return numbers[i: next_i]


res1 = part1()
print("Part 1:", res1)
res2 = part2(res1)
print("Part 2:", min(res2) + max(res2))
