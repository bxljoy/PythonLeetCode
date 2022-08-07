# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = TreeNode(-2147483648000)

    def recoverTree(self, root):
        self.traverse(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if root.val < self.pre.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.traverse(root.right)