list = [int(i) for i in input().split()]

count = [0] * (max(list) + 1)



for unit in list:
    count[unit] += 1

for unit in list:
    if count[unit] == 1:
        print(unit, end=' ')
        count[unit] = 0