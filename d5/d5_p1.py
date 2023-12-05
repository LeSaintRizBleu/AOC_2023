import re

f = open("d5/input.txt", "r")

s = [{},{},{},{},{},{},{},{}]
state = 0

for line in f:
    if line=="\n":
        if(state>0 and len(s[state-1]) != len(s[state])):
            for seed in s[state-1].values():
                if(seed not in s[state]):
                    s[state][seed] = seed
        state += 1


    if state == 0:
        for n in list(map(int,re.findall("([0-9]+)",line))):
            s[0][n] = n 

    else:
        data = list(map(int,re.findall("([0-9]+)",line)))
        if len(data)>0:
            for seed in s[state-1].values():
                if(data[1]<=seed and data[1]+data[2]>=seed):
                    s[state][seed] = seed - data[1] + data[0]

if(state>0 and len(s[state-1]) != len(s[state])):
    for seed in s[state-1].values():
        if(seed not in s[state]):
            s[state][seed] = seed

print(min(s[7].values()))