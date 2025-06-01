def isZeroArray( nums, queries):
    """
    :type nums: List[int]
    :type queries: List[List[int]]
    :rtype: bool
    """
    for ranges in queries:
        st,ed=ranges[0],ranges[1]
        # print(st,ed)
        for i in range(st,ed+1):
            if nums[i]!=0:
                nums[i]-=1
        # print(nums)
        
    for i in nums:
        if i!=0:
            return False
    
    return True

nums = [1,0,1]
queries = [[0,2]]
print(isZeroArray(nums,queries))