m = int(input())
events = []
l, r = map(int, input().split())

while not (l == 0 and r == 0):
#    if r > 0 and l < m:
    events.append((l, r))
    l, r = map(int, input().split())
events.sort()
flag = True
count = 0
right = 0
x = 0
ans = [0] * m
while right < m:
    for event in events:
        if event[0] <= x:
            if event[1] > right:
                ans[count] = event
                right = event[1]
        else:
            break
    if right > x:
        x = right
        count += 1
        ans.append(event)
    else:
        flag = False
        break    

if flag:
        print(count)
        for i in range(count):
            print(*ans[i])

else:
    print('No solution')   
