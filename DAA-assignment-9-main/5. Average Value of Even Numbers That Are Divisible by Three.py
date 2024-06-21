def average_even_divisible_by_three(nums):
    even_divisible_by_three = [num for num in nums if num % 2 == 0 and num % 3 == 0]

    if not even_divisible_by_three:
        return 0

    return sum(even_divisible_by_three) // len(even_divisible_by_three)


# Example 1
nums1 = [1, 3, 6, 10, 12, 15]
print(average_even_divisible_by_three(nums1))  # Output: 9

# Example 2
nums2 = [1, 2, 4, 7, 10]
print(average_even_divisible_by_three(nums2))  # Output: 0
