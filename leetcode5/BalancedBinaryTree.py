# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

balanced = True
class Solution:
    def __init__(self):
        global balanced
        balanced = True

    def isBalanced(self, root: [TreeNode]) -> bool:
        if root is None:
            return True
        self.maxDepth(root)
        return balanced

    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        global balanced
        if abs(left - right) > 1:
            balanced = False
        return 1 + max(left, right)
