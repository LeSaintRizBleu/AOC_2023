import re

f = open("d2/input.txt", "r")
res = 0

red = 12
green = 13
blue = 14

i=1

for line in f:
    ok = True
    r = map(int,re.findall("([0-9]*) red",line))
    g = map(int,re.findall("([0-9]*) green",line))
    b = map(int,re.findall("([0-9]*) blue",line))

    for x in r:
        if(x > red): ok = False

    for x in g:
        if(x > green): ok = False

    for x in b:
        if(x > blue): ok = False

    if(ok):
        res += i

    i+=1

print(res)