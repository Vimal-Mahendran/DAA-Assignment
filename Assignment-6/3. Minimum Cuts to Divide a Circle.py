def minimum_cuts(k):
    if k == 1:
        return 0
    n = 0
    while True:
        parts = (n * (n - 1)) // 2 + n + 1
        if parts >= k:
            return n
        n += 1

print(minimum_cuts(3)) 
print(minimum_cuts(4)) 