n, q = map(int, input().split())
nums = [int(i) for i in input().split()]
prefixsum = []
sum = 0
for num in nums:
    prefixsum.append(sum)
    sum += num 
prefixsum.append(sum)
for _ in range(q):
    l, r = map(int, input().split())
    print(prefixsum[r] - prefixsum[l-1])