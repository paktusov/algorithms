n = int(input())
seq = [int(i) for i in input().split()]

def checkisl(index, params):
    seq, x = params
    return seq[index] >= x

def checkisr(index, params):
    seq, x = params
    return seq[index] <= x 

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l        

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, checkparams):
            l = m
        else:
            r = m - 1
    return l        

m = int(input())
ans = [0] * m
nums = [int(i) for i in input().split()]
for i in range(len(nums)):
    l = lbinsearch(0, len(seq) - 1, checkisl, (seq, nums[i])) + 1
    r = rbinsearch(0, len(seq) - 1, checkisr, (seq, nums[i])) + 1
    if seq[l - 1]  == nums[i] and seq[r - 1] == nums[i]:  
        ans[i] = l, r
    else:
        ans[i] = 0, 0   

for an in ans:
    print(*an)   
