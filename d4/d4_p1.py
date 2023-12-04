import re

f = open("d4/input.txt", "r")
res = 0

for line in f:
    nMatch = 0
    n = re.findall("([0-9]{1,3})",line)
    del n[0]
    first = n[:10]
    second = n[-25:]
    for x in first:
        if(x in second):
            nMatch+=1
    if nMatch!=0:
        res += 2**(nMatch-1)

print(res)