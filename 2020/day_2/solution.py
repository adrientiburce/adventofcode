import os

dir_path = os.path.dirname(os.path.realpath(__file__))
input = open(f"{dir_path}/input.txt", "r")
lines = input.readlines()

# ======= PART ONE ========
res = 0
res2 = 0
for line in lines:
    ll = line.split(" ")
    n1, n2 = map(int, ll[0].split("-"))
    letter = ll[1][:1]
    password = ll[2]
    if n1 <= password.count(letter) <= n2:
        res += 1

# ======= PART TWO ========
    if password[n1-1] == letter and not(password[n2-1] == letter):
        res2 += 1
    elif password[n2-1] == letter and not(password[n1-1] == letter):
        res2 += 1

print(f"Part 1: valid passord : {res}/{len(lines)}")
print(f"Part 2: valid passord : {res2}/{len(lines)}")
