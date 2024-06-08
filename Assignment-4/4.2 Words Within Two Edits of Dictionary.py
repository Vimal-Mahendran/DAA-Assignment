from collections import defaultdict

def is_within_two_edits(word1, word2):
    if word1 == word2:
        return True
    if len(word1) != len(word2):
        return False
    
    edits = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            edits += 1
            if edits > 2:
                return False
    return True

def find_words_within_two_edits(queries, dictionary):
    words = set(dictionary)
    result = []
    
    for query in queries:
        if query in words:
            result.append(query)
            continue
        
        if any(is_within_two_edits(query, word) for word in words):
            result.append(query)
    
    return result

queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
output = find_words_within_two_edits(queries, dictionary)
print(output)
