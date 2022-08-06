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

    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        if root is None:
            global res
            return res
        res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return res

class Solution1:
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        res1 = []
        if root is None:
            return res1
        res1.append(root.val)
        res1.extend(self.preorderTraversal(root.left))
        res1.extend(self.preorderTraversal(root.right))
        return res1

