def count_elements(arr):
    return sum(1 for x in arr if x + 1 in arr)

arr2 = [1, 1, 3, 3, 5, 5, 7, 7]
print(count_elements(arr2))