class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidSequence(root, arr):
    def dfs(node, arr, index):
        if not node:
            return False
        if index >= len(arr) or node.val != arr[index]:
            return False
        if not node.left and not node.right and index == len(arr) - 1:
            return True
        return dfs(node.left, arr, index + 1) or dfs(node.right, arr, index + 1)
    
    return dfs(root, arr, 0)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(0)
root.left.right.left = TreeNode(0)

arr = [0, 1, 0, 1]
print(isValidSequence(root, arr))

arr = [0, 0, 0]
print(isValidSequence(root, arr))
arr = [0, 1, 1]
print(isValidSequence(root, arr))
