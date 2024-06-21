def find_odd_string(words):
    n = len(words[0])
    for i in range(n - 1):
        diff = ord(words[0][i + 1]) - ord(words[0][i])

    for word in words:
        temp_diff = [ord(word[i + 1]) - ord(word[i]) for i in range(n - 1)]
        if temp_diff != diff:
            return word


# Example 1
words1 = ["adc", "wzy", "abc"]
print(find_odd_string(words1))  # Output: "abc"

# Example 2
words2 = ["aaa", "bob", "ccc", "ddd"]
print(find_odd_string(words2))  # Output: "bob"
