import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")  # 37 & 26
    seats = []
    for l in input.read().splitlines():
        seats.append(list(l))
    return seats


seats = parse_input("input")

DIRECTIONS = {
    'up': (1, 0), 'down': (-1, 0), 'right': (0, 1), 'left': (0, -1),
    'd_up_r': (1, 1), 'd_down_r': (-1, 1), 'd_up_l': (1, -1), 'd_down_l': (-1, -1)
}


def next_round(seats: list[list], part: int, max_visible: int):
    h, w = len(seats), len(seats[0])
    next_round = [0] * h
    for i in range(h):
        next_round[i] = [0] * w
        for j in range(w):
            count = 0
            for k in DIRECTIONS:
                m = 1
                ii, jj = i+DIRECTIONS[k][0], j+DIRECTIONS[k][1]
                while(ii >= 0 and jj >= 0 and ii < h and jj < w):
                    if seats[ii][jj] == ".":
                        m += 1
                        ii, jj = i+m*DIRECTIONS[k][0], j+m*DIRECTIONS[k][1]
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


def find_stability(part: int, max_visible: int, seats=seats):
    current_seat = seats
    i = 1
    while True:
        next_seats = next_round(current_seat, part, max_visible)
        if next_seats == current_seat:
            return count_seats(next_seats)
        else:
            current_seat = next_seats
        i += 1


def test_demo():
    assert find_stability(1, 4, parse_input("demo")) == 37
    assert find_stability(2, 5, parse_input("demo")) == 26


start = time.time()
print("Part 1:", find_stability(1, 4))  # , "/ Part 2:", find_stability(2, 5))
print("--- %.4f seconds ---" % (time.time() - start))
