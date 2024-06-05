def stringShift(s, shift):
    total_shift = 0
    for direction, amount in shift:
        if direction == 0:
            total_shift -= amount
        else:
            total_shift += amount

    total_shift %= len(s)
    return s[-total_shift:] + s[:-total_shift]

s = "abcde"
shift = [[0,1],[1,2]]
print(stringShift(s, shift))
