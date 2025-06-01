# L->R
def insertionSort(n,a):
    ls=[]
    
    for i in range(1,n):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            ls.append(list(a))
            j-=1
        a[j+1]=key
    ls.append(list(a))
    # for i in ls:
    #     for j in range(n):
    #         print(i[j],end=" ")
    #     print()
    return ls
    

n=6
A=[1, 4 ,3 ,5, 6, 2]
print(insertionSort(n,A))