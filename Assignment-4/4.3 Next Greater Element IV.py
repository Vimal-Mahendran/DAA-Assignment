def second_greater(nums):
    n = len(nums)
    answer = [-1] * n
    next_greater_stack = []
    second_greater_stack = []

    for i in range(n - 1, -1, -1):
        while second_greater_stack and second_greater_stack[-1] <= nums[i]:
            second_greater_stack.pop()
        
        while next_greater_stack and next_greater_stack[-1] <= nums[i]:
            second_greater_stack.append(next_greater_stack.pop())
        
        if second_greater_stack:
            answer[i] = second_greater_stack[-1]

        next_greater_stack.append(nums[i])
    
    return answer

nums = [1, 2, 4, 3]
print(second_greater(nums))
