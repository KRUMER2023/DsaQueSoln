

def singleNonDuplicate( a):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(a)==1:
        return a[0]
    lo,hi=0,len(a)-1

    while(lo<=hi):
        mid=(lo+hi)//2
        print(mid)
        if lo==hi:
            return a[mid]
        if a[mid]!=a[mid-1] and a[mid]!=a[mid+1] :
            return a[mid]
        elif mid&1==0:
            if a[mid]==a[mid+1]:
                lo=mid+2
            else:
                hi=mid-2
        else:
            if a[mid]==a[mid-1]:
                lo=mid+1
            else:
                hi=mid-1

print(singleNonDuplicate([5,5,6,6,7]))