def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = [(candy + extraCandies) >= max_candies for candy in candies]
    return result

candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
