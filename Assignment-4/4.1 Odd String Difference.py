def find_difference_string(words):
    n = len(words[0])
    diff = [ord(words[0][i+1]) - ord(words[0][i]) for i in range(n-1)]
    
    for word in words:
        curr_diff = [ord(word[i+1]) - ord(word[i]) for i in range(n-1)]
        if curr_diff != diff:
            return word

words = ["adc", "wzy", "abc"]
print(find_difference_string(words))  # Output: "abc"
