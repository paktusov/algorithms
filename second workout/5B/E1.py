s = int(input())

a = [int(i) for i in input().split()][1:]
for i in range(len(a)):
    a[i] = a[i], i
a.sort()    

b = [int(i) for i in input().split()][1:]
for i in range(len(b)):
    b[i] = b[i], i
b.sort()

c = [int(i) for i in input().split()][1:]
for i in range(len(c)):
    c[i] = c[i], i
c.sort(key=lambda x:(x[0], -x[1]))

flag = True
answ = []

for i in range(len(a)):
    k = len(c) - 1
    for j in range(len(b)):
        while s - (a[i][0] + b[j][0]) < c[k][0] and k > 0:
            k -= 1
        if s - (a[i][0] + b[j][0]) == c[k][0]:
            answ.append((a[i][1], b[j][1], c[k][1]))
            flag = False

    
if flag:
    print(-1)
else:
    print(*min(answ))    


