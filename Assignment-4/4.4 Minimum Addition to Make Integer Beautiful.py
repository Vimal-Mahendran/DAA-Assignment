def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def make_integer_beautiful(n, target):
    current_sum = sum_of_digits(n)
    
    if current_sum <= target:
        return 0
    
    increment = 1
    while True:
        next_n = ((n // increment) + 1) * increment
        if sum_of_digits(next_n) <= target:
            return next_n - n
        increment *= 10

n = 16
target = 6
print(make_integer_beautiful(n, target))
