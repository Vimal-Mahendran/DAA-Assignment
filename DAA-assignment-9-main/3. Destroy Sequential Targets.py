def destroy_sequential_targets(nums, space):
    nums.sort()
    max_destroyed = 0
    min_seed = float('inf')

    for num in nums:
        destroyed = 1
        target = num + space
        while target in nums:
            destroyed += 1
            target += space
        if destroyed > max_destroyed or (destroyed == max_destroyed and num < min_seed):
            max_destroyed = destroyed
            min_seed = num

    return min_seed


# Example
nums = [1, 3, 5, 7, 9]
space = 2
result = destroy_sequential_targets(nums, space)
print(result)
