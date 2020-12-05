import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = input.readlines()


def isPassportValidOne(passport: dict) -> bool:
    if len(passport) < 7 or (len(passport) == 7 and "cid" in passport):
        return False
    return True


def isPassportValidTwo(passport: dict) -> bool:
    if not isPassportValidOne(passport):
        return False
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    if not(passport['hgt'].endswith('cm') or passport['hgt'].endswith('in')):
        return False
    if passport['hgt'].endswith('cm') and (int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193):
        return False
    elif passport['hgt'].endswith('in') and (int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76):
        return False
    if not passport['hcl'].startswith('#'):
        return False
    if not re.search(r'^#(?:[0-9a-f]{6})$', passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        return False
    return True


i = count1 = count2 = 0
while i < len(lines):
    passport = {}
    j = i
    while j < len(lines) and lines[j].rstrip() != "":
        elements = lines[j].rstrip().split(" ")
        for el in elements:
            key, value = el.split(":")
            passport[key] = value
        j += 1  # go to next line for passport
    count1 += isPassportValidOne(passport)
    count2 += isPassportValidTwo(passport)
    i = j + 1  # skip blank line

print(f'Part 1: {count1}; Part 2: {count2}')
