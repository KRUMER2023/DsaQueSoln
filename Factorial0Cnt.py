def Cnt(n):
    c,p = 0,5
    while n//p > 0:
        c += n // p
        p *= 5
    return c

t = int(input())
res = []
for _ in range(t):
    N = int(input())
    res.append(Cnt(N))

for r in res:
    print(r)
