def maximumXOR(n, edges, values):
    from collections import defaultdict

    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    subtree_sums = [0] * n
    
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        total = values[node]
        for neighbor in tree[node]:
            if not visited[neighbor]:
                total += dfs(neighbor)
        subtree_sums[node] = total
        return total

    dfs(0)
    
    all_sums = subtree_sums[:]
    
    max_xor = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not is_ancestor(i, j) and not is_ancestor(j, i):
                max_xor = max(max_xor, all_sums[i] ^ all_sums[j])
    
    return max_xor

def is_ancestor(ancestor, node):
    return False

n = 5
edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
values = [2,8,3,6,2,5]

print(maximumXOR(n, edges, values))
