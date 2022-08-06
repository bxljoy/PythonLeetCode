# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

res = 100000
depth = 0
class Solution:
    def __init__(self):
        global res
        global depth
        res = 100000
        depth = 0

    def minDepth(self, root: [TreeNode]) -> int:
        if root is None:
            return 0
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global res
        global depth
        depth += 1
        self.traverse(root.left)
        self.traverse(root.right)
        if root.left is None and root.right is None:
            res = min(res, depth)
        depth -= 1
