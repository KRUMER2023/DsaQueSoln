def MaxSum(a,n):
    MSum=float("-inf")
    for i in range(n):
        Sum=0
        prev=float("-inf")
        for j in range(i,n):
            if prev>=a[j]:
                i=j
                break
            Sum+=a[j]
            MSum=max(MSum,Sum)
            prev=a[j]
    
    return MSum

a=[3,6,10,1,8,9,9,8,9]
n=len(a)
print( MaxSum(a,n))
