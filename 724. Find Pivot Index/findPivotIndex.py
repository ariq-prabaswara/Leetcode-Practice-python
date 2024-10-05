def pivotIndex(nums):
    total = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        if lsum == total - lsum - nums[i]:
            return i
        lsum += nums[i]
    return -1

print(pivotIndex([1,2,-1,4,5,1,-3,5,3,4,1,-5,6,8]))