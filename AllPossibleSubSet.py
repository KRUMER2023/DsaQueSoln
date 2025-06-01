def generate(i,a):
    if i==-1:
        if len(ar)!=0:
            ls.append(list(ar))
        return
    ar.append(a[i])
    generate(i-1,a)
    ar.pop()
    generate(i-1,a)

n=int(input())
a=list(map(int,input().split( )))
# print(a)
ar=[]
ls=[]
generate(n-1,a)
ls.sort()
print(ls)