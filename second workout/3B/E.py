m = int(input())
evidences = [input() for _ in range(m)]

n = int(input())
suspects = []
length = 0
for i in range(n):
    nums = input()
    l = 0
    for evidence in evidences:
        if set(list(evidence)) <= set(list(nums)):
            l += 1
    if l > length:
        suspects = [nums]
        length = l
    elif l == length:            
        suspects.append(nums)            

print(*suspects, sep='\n')           
