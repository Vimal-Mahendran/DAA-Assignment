def nextGreaterElement(nums):
    stack, result = [], [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result

# Example
nums = [2, 4, 0, 9, 6]
output = nextGreaterElement(nums)
print(output)
