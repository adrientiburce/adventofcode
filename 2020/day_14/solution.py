import os
import time
import re
import itertools

dir_path = os.path.dirname(os.path.realpath(__file__))


def parse_input(file: str):
    input = open(f"{dir_path}/{file}.txt", "r")
    lines = input.read().splitlines()
    return lines


lines = parse_input("input")


def compute(part: int, lines=lines):
    memory_dict = {}
    mask = ""
    for l in lines:
        if l.startswith("mask"):
            mask = l[len("mask = "):]
        else:
            match = re.match(r'mem\[(.*)\] = (.*)', l)
            address, v = int(match.group(1)), int(match.group(2))

            if part == 1:
                memory_dict[address] = apply_mask(mask, v)
            elif part == 2:
                all_address = apply_mask_part2(mask, address)
                memory_dict.update({address: v for address in all_address})
    return sum(memory_dict.values())


def apply_mask(mask: str, n: int) -> int:
    bits = list(bin(n)[2:].zfill(36))  # on 36 bits
    for i, bit_mask in enumerate(mask):
        if bit_mask != "X":
            bits[i] = bit_mask
    return int("".join(bits), 2)


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def apply_mask_part2(mask: str, adress: int) -> int:
    bits_address = list(bin(adress)[2:].zfill(36))
    for i, bit_mask in enumerate(mask):
        if bit_mask != "0":
            bits_address[i] = bit_mask
    all_adress = []

    x_pos = find(bits_address, "X")
    combination = list(itertools.product(["0", "1"], repeat=mask.count("X")))

    for c in combination:
        new_adress = bits_address
        for i in range(len(c)):
            new_adress[x_pos[i]] = c[i]
        all_adress.append(int("".join(new_adress), 2))
    return all_adress


def test_demo():
    assert compute(1, parse_input("demo")) == 165
    assert compute(2, parse_input("demo2")) == 208


start = time.time()
print("Part 1:", compute(1), "/ Part 2:", compute(2))
print("--- %.4f seconds ---" % (time.time() - start))
