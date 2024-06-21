from collections import defaultdict


def is_edit_distance_one(word1, word2):
    if len(word1) != len(word2):
        return False
    count_diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 1:
                return False
    return count_diff == 1


def words_within_two_edits(queries, dictionary):
    word_dict = defaultdict(list)
    for word in dictionary:
        word_dict[len(word)].append(word)

    result = []
    for query in queries:
        if query in dictionary:
            result.append(query)
            continue
        if query in word_dict[len(query)]:
            result.append(query)
            continue
        for word in word_dict[len(query)]:
            if is_edit_distance_one(query, word) or is_edit_distance_one(query, word):
                result.append(query)
                break
    return result


# Example
queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
output = words_within_two_edits(queries, dictionary)
print(output)
