brackets = list(input())
#print(brackets)
prefixsum = [0] * (len(brackets) + 1)
for i in range(1, len(brackets) + 1):
    if brackets[i-1] == ')':
        prefixsum[i] = prefixsum[i-1] - 1
    elif brackets[i-1] == '(':
        prefixsum[i] = prefixsum[i-1] + 1
#print(prefixsum[1:])
if min(prefixsum[1:]) == 0:
    print('YES')
else:
    print('NO')               