MOD = 10**9 + 7

def numberWays(hats):
    from collections import defaultdict

    n = len(hats)
    all_mask = (1 << n) - 1

    hat_to_people = defaultdict(list)
    for person, hat_list in enumerate(hats):
        for hat in hat_list:
            hat_to_people[hat].append(person)

    dp = [0] * (1 << n)
    dp[0] = 1

    for hat in range(1, 41):
        if hat in hat_to_people:
            for mask in range(all_mask, -1, -1):
                for person in hat_to_people[hat]:
                    if mask & (1 << person):
                        dp[mask] = (dp[mask] + dp[mask ^ (1 << person)]) % MOD

    return dp[all_mask]

hats = [[3, 4], [4, 5], [5]]
print(numberWays(hats))
