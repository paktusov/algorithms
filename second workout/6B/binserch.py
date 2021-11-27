

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x

def findfirstge(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans        

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(checkparams):
            r = m
        else:
            l = m + 1

def rbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(checkparams):
            l = m
        else:
            r = m - 1