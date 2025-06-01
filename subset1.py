def generate(i,ar,tkn,n,x):
    if i ==n:
        if check(ar,x):
            ms.append(list(ar))
        return

    for j in range(1,n+1):
        if not tkn[j]:
            ar[i]=j
            tkn[j]=1
            generate(i+1,ar,tkn,n,x)
            tkn[j]=0

# [1,3,2,5,4]
# [3,4,1,2]
def check(ar,x):
    i=1
    for k in ar:
        if k|i==x:
            return True
        i+=1
    return False

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    ar=[0]*n
    tkn=[0]*(n+1)
    ms=[]
    generate(0,ar,tkn,n,x)
    if len(ms)==0:
        for i in range(1,x):
            print(i,end=" ")
    else:
        for z in ms[0]:
          print(z,end=" ")
        
    ms.clear()
    print()
    # print(check([3,4,1,2],1))
