import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = []
for l in input.readlines():
    lines.append(l.rstrip())


def handle_seat(seat: str) -> int:
    n_row = do_dichotomy(seat[:7], 0, 127)
    n_column = do_dichotomy(seat[7:], 0, 7)
    return n_row * 8 + n_column


def do_dichotomy(directions: str, bound_left: int, bound_right: int) -> int:
    if len(directions) > 0:
        next_direction = directions[0]
        if next_direction == "F" or next_direction == "L":
            return do_dichotomy(directions[1:], bound_left, math.floor((bound_left + bound_right) / 2))
        elif next_direction == "B" or next_direction == "R":
            return do_dichotomy(directions[1:], math.ceil((bound_right + bound_left) / 2), bound_right)
    return(bound_left)


seats_ids = []
for seat in lines:
    seats_ids.append(handle_seat(seat))
seats_ids = sorted(seats_ids)

my_seat, i = -1, 0
while i < len(seats_ids):
    if seats_ids[i] + 1 != seats_ids[i+1]:
        my_seat = seats_ids[i]+1
        break
    i += 1

print(f"Part 1: {max(seats_ids)}, Part  2: {my_seat}")
