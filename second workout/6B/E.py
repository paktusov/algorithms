n, k = map(int, input().split())
seq = sorted([int(i) for i in input().split()])
#print(seq)
def checkisl(m, params):
    seq, k = params
    count = 0
    l = seq[0]
    r = seq[0] - 1
    for x in seq:
        if x > r:
            count += 1
            r = x + m
    return count <= k

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l        

lb = 0
rb = seq[-1] - seq[0]

length = rbinsearch(lb, rb, checkisl, (seq, k))
print(length)