import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
numbers = list(map(int, input.read().splitlines()))

numbers.sort()
numbers = [0] + numbers  # charging outlet
numbers = numbers + [max(numbers) + 3]  # device adapterr


def part_1():
    diff_1 = diff_3 = 0
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == 1:
            diff_1 += 1
        elif numbers[i+1] - numbers[i] == 3:
            diff_3 += 1

    return diff_1*diff_3


def part_2():
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


print("Part 1:", part_1(), "; Part 2:", part_2())
