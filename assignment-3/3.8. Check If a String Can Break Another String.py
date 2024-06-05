def checkIfCanBreak(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    can_s1_break_s2 = all(c1 >= c2 for c1, c2 in zip(s1_sorted, s2_sorted))
    
    can_s2_break_s1 = all(c2 >= c1 for c1, c2 in zip(s1_sorted, s2_sorted))
    
    return can_s1_break_s2 or can_s2_break_s1

s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))

s1 = "abe"
s2 = "acd"
print(checkIfCanBreak(s1, s2))

s1 = "leetcodee"
s2 = "interview"
print(checkIfCanBreak(s1, s2))
