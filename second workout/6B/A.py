n = int(input())
seq = [int(i) for i in input().split()]
seq.sort()

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

k = int(input())
ans = [0] * k
for i in range(k):
    ln, rn = [int(i) for i in input().split()]
    l = lbinsearch(0, len(seq) - 1, checkisl, (seq, ln))
    r = rbinsearch(0, len(seq) - 1, checkisr, (seq, rn))
    if seq[l] > rn or seq[r] < ln:
        ans[i] = 0
    else:          
        ans[i] = r - l + 1

print(*ans)    

    
