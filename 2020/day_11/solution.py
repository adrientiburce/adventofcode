import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
seats = []
for l in input.read().splitlines():
    seats.append(list(l))
h, w = len(seats), len(seats[0])


dirs = {'up': (1, 0), 'down': (-1, 0), 'right': (0, 1), 'left': (0, -1),
        'd_up_r': (1, 1), 'd_down_r': (-1, 1), 'd_up_l': (1, -1), 'd_down_l': (-1, -1)
        }

full_seats = [0] * h
for i in range(h):
    full_seats[i] = [0] * w
    for j in range(w):
        full_seats[i][j] = ("#" if seats[i][j] == "L" else ".")


def next_round(seats: list[list], part: int, max_visible: int):
    next_round = [0] * h
    for i in range(h):
        next_round[i] = [0] * w
        for j in range(w):
            count = 0
            for k in dirs:
                m = 1
                ii, jj = i+dirs[k][0], j+dirs[k][1]
                while(ii >= 0 and jj >= 0 and ii < h and jj < w):
                    if seats[ii][jj] == ".":
                        m += 1
                        ii, jj = i+m*dirs[k][0], j+m*dirs[k][1]
                    else:
                        count += seats[ii][jj] == "#"
                        break
                    if part == 1:
                        break
            if seats[i][j] == "L" and count == 0:
                next_round[i][j] = "#"
            elif seats[i][j] == "#" and count >= max_visible:
                next_round[i][j] = "L"
            else:
                next_round[i][j] = seats[i][j]
    return next_round


def count_seats(seats):
    total = 0
    for l_seats in seats:
        total += l_seats.count("#")
    return total


def find_stability(part: int, max_visible: int):
    current_seat = full_seats
    i = 1
    while True:
        next_seats = next_round(current_seat, part, max_visible)
        if next_seats == current_seat:
            return count_seats(next_seats)
        else:
            current_seat = next_seats
        i += 1


print("Part 1:", find_stability(1, 4), ", Part 2:", find_stability(2, 5))
