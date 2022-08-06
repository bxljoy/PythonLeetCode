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

    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global res
        self.traverse(root.left)
        self.traverse(root.right)
        res.append(root.val)

    def postorderTraversal2(self, root: [TreeNode]) -> [int]:
        if root is None:
            global res
            return res

        self.postorderTraversal2(root.left)
        self.postorderTraversal2(root.right)
        res.append(root.val)
        return res


