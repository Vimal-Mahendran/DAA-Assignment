def differenceOnesZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_ones = [0] * rows
    row_zeros = [0] * rows
    col_ones = [0] * cols
    col_zeros = [0] * cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_ones[i] += 1
                col_ones[j] += 1
            else:
                row_zeros[i] += 1
                col_zeros[j] += 1
    
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = (row_ones[i] + col_ones[j]) - (row_zeros[i] + col_zeros[j])
    
    return result

matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]

result = differenceOnesZeros(matrix)
for row in result:
    print(row)
