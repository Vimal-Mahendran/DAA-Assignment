def min_append_to_make_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1
    return len(t) - j

s1 = "coaching"
t1 = "coding"
print(min_append_to_make_subsequence(s1, t1))
