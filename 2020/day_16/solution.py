import os
import time
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    lines = open(f"{dir_path}/{file}.txt", "r").read().splitlines()
    limits, tickets, my_ticket = [], [], []
    handle_limit, i = True, 0
    field_pos = {}
    while i < len(lines):
        line = lines[i]
        if line == "":
            i += 2
            handle_limit = False
            continue
        if handle_limit:
            limits.append(list(map(int, re.findall(r'(\d+)', line))))
            field_pos[line.split(":")[0]] = []
        elif my_ticket == []:
            my_ticket = list(map(int, line.split(",")))
        else:
            tickets.append(list(map(int, line.split(","))))
        i += 1
    return limits, tickets, field_pos, my_ticket


limits, tickets, field_pos, my_ticket = parse_input("input")


def is_valid(n: int, limit: tuple):
    return limit[0] <= n <= limit[1] or limit[2] <= n <= limit[3]


def part_1(limits=limits, tickets=tickets):
    valid_ticket = tickets[:]
    res = 0
    for i, ticket in enumerate(tickets):
        # check every ticket number
        for n in ticket:
            valid_n = False
            for limit in limits:
                if is_valid(n, limit):
                    valid_n = True
                    break  # pass to next n in ticket
                else:
                    continue
            if not valid_n:
                res += n
                valid_ticket.remove(ticket)
                break  # skip end of ticket
    return res, valid_ticket


def part_2(limits=limits, tickets=tickets, field_pos=field_pos, my_ticket=my_ticket):
    for j, field in enumerate(field_pos):
        limit = limits[j]
        # test ith element
        for i in range(len(field_pos)):
            valid_for_all = True
            for ticket in tickets:
                if is_valid(ticket[i], limit):
                    continue
                else:
                    valid_for_all = False
                    break
            if valid_for_all:
                old_pos = field_pos[field]
                old_pos.append(i)
                field_pos[field] = old_pos
    final_pos = find_final_pos(field_pos)
    res = 1
    for field, pos in final_pos.items():
        if field.startswith("departure"):
            res *= my_ticket[pos[0]]
    return res


def find_final_pos(field_pos):
    if all([len(x) == 1 for x in field_pos.values()]):
        return field_pos
    uniques = []
    for p in field_pos.values():
        if len(p) == 1:
            uniques.append(p[0])
    # remove all unique from every list
    for k, p in field_pos.items():
        if len(p) == 1:
            continue
        new = [x for x in p if x not in uniques]
        field_pos[k] = new
    return find_final_pos(field_pos)


def test_demo():
    limits, tickets, field_pos, my_ticket = parse_input("demo")
    assert part_1(limits, tickets)[0] == 71


start = time.time()
res_1, valid_tickets = part_1()
print("Part 1:", res_1, "/ Part 2:", part_2(tickets=valid_tickets))
print("--- %.4f seconds ---" % (time.time() - start))
