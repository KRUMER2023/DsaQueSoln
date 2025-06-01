# Start at the rightmost index. Store the value of . Compare this to each element to the left until a smaller value is reached.
# R->L
def insertionSort(n,a):
    ls=[]
    
    for i in range(n-1,-0,-1):
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
    

n=5
A=[2, 4 ,6 ,8, 3]
print(insertionSort(n,A))

