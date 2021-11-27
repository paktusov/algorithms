n, m = map(int, input().split())
x = [int(i) + 1 for i in input().split()]
for i in range(n):
    x[i] = (x[i], i+1)
x.sort()
y = [int(i) for i in input().split()]
for i in range(m):
    y[i] = (y[i], i+1)
y.sort()
count = 0
answ = [0] * (n)
last = 0

print(*x)
print(*y)
for first in range(n):
    while last < m and y[last][0] < x[first][0]:
        last += 1
    if last < m:
        count += 1
        answ[(x[first][1] - 1)] = y[last][1]
        last += 1
    
print(count)   
print(*answ)
    
