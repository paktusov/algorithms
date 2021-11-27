n, q = map(int, input().split())
nums = [int(i) for i in input().split()]
#prefixsum = []
#sum = 0

def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum

def psq(prefixsum, l, r):
    return prefixsum[r] - prefixsum[l-1]

#for num in nums:
#    prefixsum.append(sum)
#    sum += num 
#prefixsum.append(sum)
#print(prefixsum)
prefixsum = makeprefixsum(nums)

for _ in range(q):
    l, r = map(int, input().split())
    
    print(psq(prefixsum, l, r))