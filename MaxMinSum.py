def miniMaxSum(arr):
    # Write your code here
    Max,Min=float("-inf"),float("inf")
    Tsum=sum(arr)
    for i in arr:
        temp=Tsum-i
        Max=max(Max,temp)
        Min=min(Min,temp)
    return list((Min,Max))
print(miniMaxSum([1,2,3,4,5]))