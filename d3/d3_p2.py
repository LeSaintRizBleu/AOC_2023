f = open("d3/input.txt", "r")
txt = f.read().split("\n")

res = 0
n=0
ok = False

def isGear(t, row, col):
    if(t[row][col]=="*"):
        x = 0
        for i in range(row - 1, row + 2):
            ok = True
            for j in range(col - 1, col + 2):
                if 0 <= i < len(t) and 0 <= j < len(t[i]):
                    if t[i][j].isdigit():
                        if ok: 
                            x += 1
                            ok = False
                    else : ok = True
        return x==2
    return False

def gearValue(t,row,col):
    x = 1
    for i in range(row - 1, row + 2):
        ok = True
        for j in range(col - 1, col + 2):
            if ok and 0 <= i < len(t) and 0 <= j < len(t[i]) and t[i][j].isdigit():
                off = 0
                n = 0
                #get the offset
                while 0 <= i < len(t) and 0 <= j+off < len(t[i]) and t[i][j+off].isdigit():
                    off -= 1
                    ok = False
                off += 1
                #read the whole number
                while 0 <= i < len(t) and 0 <= j+off < len(t[i]) and t[i][j+off].isdigit():
                    n = n*10 + int(t[i][j+off])
                    off+=1
                if(n>0):
                    x *= n
            else:
                if(t[i][j].isdigit() == False):
                   ok = True
    return x

nLine = len(txt)
for i in range(nLine):

    nChar = len(txt[i])
    for j in range(nChar):
        if(isGear(txt,i,j)):
            res += gearValue(txt,i,j)

print(res)
