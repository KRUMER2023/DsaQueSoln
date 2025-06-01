ls=[]
def SS(i, a, n, ar):
    if i == n:
        if ar:             #and sum(list(ar))==6 add this for SS whose sum is 6  
            ls.append(list(ar))
        return
    ar.append(a[i])
    SS(i + 1, a, n, ar)
    ar.pop()
    SS(i + 1, a, n, ar)

a = [1, 2, 3,4,5]
SS(0, a, len(a), [])
ls.sort()
print(ls)
