def minOperations(nums):
    n = len(nums)
    count = 0
    for i in range(n-1):
        if nums[i] != i:
            nums[nums.index(i)], nums[i] = nums[i], nums[nums.index(i)]
            count += 1
    return count

nums = [2, 0, 1, 3]
print(minOperations(nums))
