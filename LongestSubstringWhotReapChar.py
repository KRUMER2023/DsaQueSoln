Mx=0

def SS(s,i,n):
    global Mx
    for i in range(n):
        k=""
        o=set()
        for j in range(i,n):
            if s[j] in o:
                break
            o.add(s[j])
            k+=s[j]
        Mx=max(Mx,len(k))
            
s="abcabcbb"
n=len(s)
SS(s,0,n)
print(Mx)