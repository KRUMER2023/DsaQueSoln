import bisect

def find_floor(arr, x):
    idx = bisect.bisect_right(arr, x)
    return arr[idx - 1] if idx > 0 else -1

a=[1,2,5,6,10,15,20]
print(find_floor(a,3))