# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
res = True
tmp = -1
class Solution:
    def __init__(self):
        global res
        global tmp
        res = True
        tmp = -1

    def isUnivalTree(self, root: [TreeNode]) -> bool:
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global res
        global tmp
        if tmp == -1:
            tmp = root.val
        if tmp != root.val:
            res = False
        self.traverse(root.left)
        self.traverse(root.right)

