n = int(input())
events = []

for i in range(n):
    l, r = map(int, input().split())
    events.append((l, -1))
    events.append((r, 1))
events.sort()

full = 0
length = 0
for i in range(len(events)):
    if full > 0:
        length += events[i][0] - events[i-1][0]
    if events[i][1] == -1:
        full += 1
    elif events[i][1] == 1:
        full -= 1

print(length)                