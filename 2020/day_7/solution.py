import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = input.read().splitlines()

SHINY_GOLD = 'shiny gold'


def extract_number_and_color(data: str) -> [int, str]:
    number = int(data[0])
    color = data[2:]  # remove space
    return number, color


def clean_data(data: str) -> str:
    return data.replace('bags', '').replace('bag', '').replace('.', '').strip()


def extract_data(lines) -> dict:
    contains = {}
    for line in lines:
        bag, bags_contained = line.split('contain')
        bag = clean_data(bag)

        if 'no other bags' in line:
            bags_contained = []
        else:
            bags_contained = [
                extract_number_and_color(clean_data(bag))
                for bag in bags_contained.split(',')
            ]

        contains.update({bag: bags_contained})
    return contains


def invert_relationship(contains: dict) -> dict:
    contained_by = {}
    for key in contains.keys():
        for number, color in contains[key]:
            if color not in contained_by:
                contained_by[color] = []
            contained_by[color].append((number, key))

    return contained_by


def solve_part1(contains):
    contained_by = invert_relationship(contains)
    visited_bags = set(SHINY_GOLD)
    color_queue = [SHINY_GOLD]
    i = 0
    while i < len(color_queue):
        current_color = color_queue[i]
        if current_color in contained_by:
            for _number, color in contained_by[current_color]:
                if color not in visited_bags:
                    color_queue.append(color)
                    visited_bags.add(color)
        i += 1
    return len(color_queue) - 1


def solve_part2(contains):
    count = 0
    color_queue = [SHINY_GOLD]
    multiplier_queue = [1]
    i = 0
    while i < len(color_queue):
        current_color = color_queue[i]
        if current_color in contains:
            for number, color in contains[current_color]:
                color_queue.append(color)
                multiplier_queue.append(multiplier_queue[i] * number)
                count += multiplier_queue[i] * number
        i += 1
    return count


print("Part 1:", solve_part1(extract_data(lines)))
print("Part 2:", solve_part2(extract_data(lines)))
