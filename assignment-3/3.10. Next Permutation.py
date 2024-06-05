def nextPermutation(nums):
    n = len(nums)
    
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i == -1:
        nums.reverse()
        return
    
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1:] = reversed(nums[i + 1:])

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)

nums = [3, 2, 1]
nextPermutation(nums)
print(nums)
nums = [1, 1, 5]
nextPermutation(nums)
print(nums)