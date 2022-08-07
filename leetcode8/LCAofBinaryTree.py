# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p.val, q.val)

    def find(self, root, val1, val2):
        if not root:
            return None
        if root.val == val1 or root.val == val2:
            return root
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        if left and right:
            return root
        if left:
            return left
        else:
            return right
