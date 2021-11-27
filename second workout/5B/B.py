n = int(input())
nums = [int(i) for i in input().split()]

prefixsum = [0] * (n + 1)
mi = prefixsum[0]
ma = -1000000000
msum = nums[0]

for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i-1] + nums[i-1]

    if prefixsum[i-1] < mi:
        mi = prefixsum[i-1]

    if prefixsum[i] - mi > msum:
        msum = prefixsum[i] - mi
    
#    if prefixsum[i] > ma:
#        ma = prefixsum[i]
#        s = ma - mi
#        su.append(s)
    

#print(prefixsum[:])
print(msum)