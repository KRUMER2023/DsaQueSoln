
a=[2,5,3,7]
k=15
n=len(a)

def can_partition(nums, target,n):
    
    # Iterate over all non-empty, non-full subsets
    for mask in range(1, (1 << n) - 1):
        prod1 = 1
        subset1 = []
        subset2 = []
        
        for i in range(n):
            if (mask >> i) & 1:
                prod1 *= nums[i]
                subset1.append(nums[i])
            else:
                subset2.append(nums[i])
        
        if prod1 == target:
            prod2 = 1
            for num in subset2:
                prod2 *= num
            if prod2 == target:
                return True
    return False

print(can_partition(a,k,n))