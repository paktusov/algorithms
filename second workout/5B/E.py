s = int(input())

dicta = {}
a = [int(i) for i in input().split()][1:]
for i in range(len(a)):
    if a[i] not in dicta:
        dicta[a[i]] = i


dictb = {}
b = [int(i) for i in input().split()][1:]
for i in range(len(b)):
    if b[i] not in dictb:
        dictb[b[i]] = i

dictc = {}
c = [int(i) for i in input().split()][1:]
for i in range(len(c)):
    if c[i] not in dictc:
        dictc[c[i]] = i

flag = True

for keya in dicta:
    if not flag:
        break
    for keyb in dictb:
        answ = s - (keya + keyb)
        if answ in dictc:
            print(dicta[keya], dictb[keyb], dictc[answ])
            flag = False
            break
    
if flag:
    print(-1)


