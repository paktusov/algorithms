n = int(input())
dict = {}
for i in range(n):
    color, count = map(int, input().split())
    if color not in dict:
        dict[color] = 0
    dict[color] += count

for key in sorted(dict):
    print(key, dict[key])        