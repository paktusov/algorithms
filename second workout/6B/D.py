a, k, b, m, x = map(int, input().split())

def checkisl(d, params):
    a, k, b, m, x = params
    return (d - (d//k)) * a + (d - (d//m)) * b >= x

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

dmax = x * 3 // a + 1

d = lbinsearch(0, dmax, checkisl, (a, k, b, m, x))   
print(d) 
