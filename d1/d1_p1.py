f = open("d1/input.txt", "r")
res = 0

for line in f:

    for char in line:
        if char.isdigit():
            res += int(char) * 10
            break

    for char in reversed(line):
        if char.isdigit():
            res += int(char)
            break

f.close()            
print(res)