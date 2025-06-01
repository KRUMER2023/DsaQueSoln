def countingSort(arr,n):
    # Write your code here
    cnt=[0]*100
    for i in arr:
        cnt[i]+=1
    ls=[]
    for i in range(100):
        for j in range(cnt[i]):
            ls.append(i)
    return ls

n=5
A=[10,2,1,36,1]
print(countingSort(A,n))