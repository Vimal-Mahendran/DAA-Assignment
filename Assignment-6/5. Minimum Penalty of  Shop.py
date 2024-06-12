def bestClosingTime(customers):
    n = len(customers)
    
    open_penalty = [0] * (n + 1)
    for i in range(1, n + 1):
        open_penalty[i] = open_penalty[i - 1] + (1 if customers[i - 1] == 'N' else 0)
    
    close_penalty = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        close_penalty[i] = close_penalty[i + 1] + (1 if customers[i] == 'Y' else 0)
    
    min_penalty = float('inf')
    best_hour = 0
    for j in range(n + 1):
        penalty = open_penalty[j] + close_penalty[j]
        if penalty < min_penalty:
            min_penalty = penalty
            best_hour = j
    
    return best_hour

print(bestClosingTime("YYNY"))