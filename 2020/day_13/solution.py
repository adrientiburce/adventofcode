import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    input_lines = input.read().splitlines()
    t0 = int(input_lines[0])

    buses = {}
    for i, bus_id in enumerate(input_lines[1].split(",")):
        if bus_id == "x":
            continue
        else:
            buses[int(bus_id)] = i
    return t0, buses


t0, buses = parse_input("input")


def part_1(t0=t0, buses=buses):
    bus_chosen = 0
    wait_time = t0
    for t_bus in buses.keys():
        bus_wait_time = t_bus - t0 % t_bus
        if bus_wait_time < wait_time:
            wait_time = bus_wait_time
            bus_chosen = t_bus
    return wait_time*bus_chosen


def part_2(buses=buses):
    min_value = 0
    running_product = 1
    for bus_id in buses.keys():
        bus_offset = buses[bus_id]
        while (min_value + bus_offset) % bus_id != 0:
            min_value += running_product
        running_product *= bus_id
    return min_value


def test_demo():
    t0, buses = parse_input("demo")
    assert part_1(t0, buses) == 295
    assert part_2(buses) == 1068781


start = time.time()
print("Part 1:", part_1(), "/ Part 2:", part_2())
print("--- %.4f seconds ---" % (time.time() - start))
