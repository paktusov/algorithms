n = int(input())
events = [0] * 2* n
for i in range(0, 2*n, 2):
    t, l = map(int, input().split())
    events[i] = (t, 1)
    events[i+1] = (t+l, -1)
events.sort()
work = 0
maxwork = 0
for event in events:
    if event[1] == 1:
        work += 1
    elif event[1] == -1:
        work -= 1
    maxwork = max(work, maxwork)

print(maxwork)            