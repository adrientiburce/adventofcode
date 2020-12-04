import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f'{dir_path}/input.txt', 'r')
n1, n2 = map(int, input.read().split("-"))


# ===== PART ONE =====
def isValid(password: str) -> bool:
    haveAdjacent = False
    if len(password) != 6:
        return False
    for i in range(5):
        if int(password[i+1]) < int(password[i]):
            return False
        if password[i+1] == password[i]:
            haveAdjacent = True
    return haveAdjacent

# print(isValid("111111"))
# print(isValid("223450"))
# print(isValid("123789"))

# ===== PART TWO =====


def isValidTwo(password: str) -> bool:
    haveAdjacent = False
    if len(password) != 6:
        return False
    for i in range(5):
        if int(password[i+1]) < int(password[i]):
            return False
        if i != 4 and i != 0:
            if password[i+1] == password[i] and password[i+1] != password[i+2] and password[i-1] != password[i]:
                haveAdjacent = True
        elif i == 4:
            if password[i+1] == password[i] and password[i-1] != password[i]:
                haveAdjacent = True
        elif i == 0:
            if password[i+1] == password[i] and password[i+1] != password[i+2]:
                haveAdjacent = True
    return haveAdjacent


count = 0
for i in range(n1, n2 + 1):
    if isValidTwo(str(i)):
        count += 1
print(count)  # 763
