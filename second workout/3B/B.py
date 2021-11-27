list = [int(i) for i in input().split()]
s = set()
for unit in list:
    if unit in s:
        print('YES')
    else:
        print('NO')
        s.add(unit)
