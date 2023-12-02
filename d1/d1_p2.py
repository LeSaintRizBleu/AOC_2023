f = open("j1.txt", "r")
res = 0

digit = {"one":"one1one", "two":"two2two", "three":"three3three", "four":"four4four", "five":"five5five",
         "six":"six6six", "seven":"seven7seven", "eight":"eight8eight", "nine":"nine9nine"}

for line in f:

    for n in digit:
        line = line.replace(n,digit[n])

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


