import re

f = open("d2/input.txt", "r")
res = 0

for line in f:
    r = map(int,re.findall("([0-9]*) red",line))
    g = map(int,re.findall("([0-9]*) green",line))
    b = map(int,re.findall("([0-9]*) blue",line))

    res += max(r) * max(g) * max(b)

print(res)