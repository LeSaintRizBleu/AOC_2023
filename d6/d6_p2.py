import re

f = open("d6/input.txt", "r")

time = 53837288
distance = 333163512891532

res = 0

for x in range(time+1):
    timePress = time - x
    d = (time - timePress) * timePress
    if(d > distance):
        res += 1

print(res)