# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)

class Solution1:
    def invertTree1(self, root):
        if root is None:
            return
        left = self.invertTree1(root.left)
        right = self.invertTree1(root.right)
        root.left = right
        root.right = left
        return root


