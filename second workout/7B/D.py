n, m = map(int, input().split())
a = sorted([int(i) for i in input().split()])
segms = [0] * m
events = []
count = 0

for ai in a:
    events.append((ai, 0, -1))

for i in range(m):
    l, r = map(int, input().split())
    segms[i] = [l, r, 0]
    events.append((l, -1, i))
    events.append((r, 1, i))

events.sort()

for event in events:
    if event[1] == -1:
       segms[event[2]][2] = count
    elif event[1] == 1:
        segms[event[2]][2] = count - segms[event[2]][2]
    elif event[1] == 0:
        count += 1       

for segm in segms:
    print(segm[2], end = ' ')    
