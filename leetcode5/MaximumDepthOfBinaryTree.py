# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        depth = max(leftDepth, rightDepth) + 1
        return depth

res = 0
depth = 0
class Solution1:
    def __init__(self):
        global res
        global depth
        res = 0
        depth = 0

    def maxDepth(self, root: [TreeNode]) -> int:
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global depth
        global res
        depth = depth + 1
        if (root.left is None) and (root.right is None):
            res = max(res, depth)
        self.traverse(root.left)
        self.traverse(root.right)
        depth = depth - 1





