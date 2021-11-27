def checkrootpos(root, params):
    a, b, c, d = params
    return a * root**3 + b * root**2 + c * root + d > 0

def checkrootneg(root, params):
    a, b, c, d = params
    return a * root**3 + b * root**2 + c * root + d < 0    

def fbinsearch(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, params):
            r = m
        else:
            l = m
    return l    

a, b, c, d = map(int, input().split())
eps = 0.0000000001
l = -10000000
r = 10000000
if a > 0:
    x = fbinsearch(l, r, eps, checkrootpos, (a, b, c, d))
else:
    x = fbinsearch(l, r, eps, checkrootneg, (a, b, c, d))
print(x)