import re

f = open("d4/input.txt", "r")
nCard = 192
cpy = [1] * nCard
res = 0
curr = 0

for line in f:
    nMatch = 0
    n = re.findall("([0-9]{1,3})",line)
    del n[0]

    first = n[:10]
    second = n[-25:]
    
    for x in first:
        if(x in second):
            nMatch+=1

    x = cpy[curr]
    for i in range(curr, nMatch+curr):
        if i+1 < nCard:
            cpy[i+1] += x
    
    curr+=1

print(sum(cpy))