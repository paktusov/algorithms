nums = [int(i) for i in input().split()]

prefixsum = [0] * (len(nums) + 1)
mi = prefixsum[0]
ma = -100000
msum = nums[0]

for i in range(1, len(nums) + 1):
    prefixsum[i] = prefixsum[i-1] + nums[i-1]

    if prefixsum[i-1] < mi:
        mi = prefixsum[i-1]

    if prefixsum[i] - mi > msum:
        msum = prefixsum[i] - mi

print(msum)