import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = (input.read() + "\n").replace("\n", " ").split("  ")

count = 0
for line in lines:
    group_goods = set()
    for goods in line.split(" "):
        group_goods.update(list(goods))
    count += len(group_goods)
print(f'Part 1: {count}')

count = 0
for line in lines:
    group_goods = []
    for goods in line.split(" "):
        group_goods.append(set(list(goods)))
    count += len(set.intersection(*group_goods))
print(f'Part 2: {count}')
