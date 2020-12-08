import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = []
for l in input.read().splitlines():
	inst, i = l.split(" ")
	lines.append((inst, int(i)))


def get_last_acc(instructions: list) -> (int, bool):
	visited = [0] * len(instructions)
	i = res = 0
	while i < len(instructions):
		instruction, num = instructions[i]
		visited[i] += 1
		if 2 in visited:
			break
		if instruction == "nop":
			i += 1
		elif instruction == "jmp":
			i += num
		else:
			res += num
			i += 1
	return res, visited[-1] == 1

print("Part 1: ", get_last_acc(lines)[0])


def find_correct_instructions():
	is_done, j = False, 0
	while j < len(lines) and not is_done:
		instruction, num = lines[j]
		new_instructions = lines[:]
		if instruction == "acc":
			j += 1
			continue
		elif instruction == "nop":
			new_instructions[j] = ("jmp", num)
		else:
			new_instructions[j] = ("nop", num)
		res, is_done = get_last_acc(new_instructions)
		j += 1
	return res

print("Part 2: ", find_correct_instructions())