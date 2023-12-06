import re

f = open("d6/input.txt", "r")

AllTime = list(map(int,re.findall("([0-9]+)",f.readline() )))
AllDistances = list(map(int,re.findall("([0-9]+)",f.readline() )))

res = 1
n = len(AllTime)

for i in range(n):
    temp = 0
    for x in range(AllTime[i]+1):
        timePress = AllTime[i] - x
        distance = (AllTime[i] - timePress) * timePress
        if(distance > AllDistances[i]):
            temp += 1
    res *= temp

print(res)