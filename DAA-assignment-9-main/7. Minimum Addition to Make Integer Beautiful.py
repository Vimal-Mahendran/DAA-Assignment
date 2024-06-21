def minAddToMakeBeautiful(n, target):
    digit_sum = sum(int(d) for d in str(n))
    return max(0, (target - digit_sum) // 9 + ((target - digit_sum) % 9 != 0))

# Test the function with examples
print(minAddToMakeBeautiful(16, 6))  # Output: 4
print(minAddToMakeBeautiful(467, 6))  # Output: 33
print(minAddToMakeBeautiful(1, 1))  # Output: 0
