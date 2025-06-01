def generate(a,i,ar):
    if i==len(a):
        ar.append(list(a))
        return 
    
    for j in range(i,n):
        a[i],a[j]=a[j],a[i]
        generate(a,i+1,ar)
        a[j],a[i]=a[i],a[j]

nums=[1,2,3]
ar=[]
n=len(nums)
generate(nums,0,ar)
print(ar)
