f = open("d3/input.txt", "r")
txt = f.read().split("\n")

res = 0
n=0
ok = False

def isValid(t, row, col):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(t) and 0 <= j < len(t[i]):
                if t[i][j] not in ('0','1','2','3','4','5','6','7','8','9','.'):
                    return True 
    return False

nLine = len(txt)
for i in range(nLine):

    nChar = len(txt[i])
    for j in range(nChar):

        if txt[i][j].isdigit():
            n = n*10 + int(txt[i][j])
            ok = ok or isValid(txt,i,j)

        else:
            if(ok): res += n
            n = 0
            ok = False

    if(ok): res += n
    n = 0
    ok = False

print(res)