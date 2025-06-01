# Generate the subStrings , prt sum of 3 largest primes , if no. of primes < 3 prt sum of remaining

def Prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def subS(s):
    ans=[]
    n=len(s)
    
    for i in range(n):
        for j in range(i,n):
            num=int(s[i:j+1])
            if Prime(num):
                ans.append(num)
    return ans

s="111"
res=subS(s)
res=list(set(res))
res.sort()
if len(res)<3:
    print(sum(res))
else:
    print(res[-1]+res[-2]+res[-3])