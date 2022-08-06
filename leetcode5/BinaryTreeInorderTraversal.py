# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
res = []
class Solution:
    def __init__(self):
        global res
        res = []

    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        if root is None:
            global res
            return res
        self.inorderTraversal(root.left)
        res.append(root.val)
        self.inorderTraversal(root.right)
        return res

class Solution1:
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return res
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
