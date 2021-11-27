import math

n = int(input())
corners = [0] * 2 * n
segments = set()
r1max = 0
r2min = 10**6
dif = []
for i in range(0, 2*n, 2):
    r1, r2, q1, q2 = map(float, input().split())
    r1max = max(r1max, r1)
    r2min = min(r2min, r2)
    corners[i] = (q1,-1, (i)/2)
    corners[i+1] = (q2, 1, (i)/2)
corners.sort()
count = 0
for i in range(len(corners)):
    if corners[i][1] == -1:
        segments.add(corners[i][2])
        count += 1
    elif corners[i][1] == 1 and corners[i][2] in segments:
        count -= 1
for i in range(len(corners)):
    if corners[i][1] == -1:
        count += 1
    elif corners[i][1] == 1:
        count -= 1
    if count == n:
        if i < len(corners) - 1:
            dif.append(corners[i+1][0] - corners[i][0])
        else:
            dif.append(corners[0][0] + (2 * math.pi - corners[i][0]))

s = (r2min**2 - r1max**2) * sum(dif) / 2
print(s)