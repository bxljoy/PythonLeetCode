# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: [TreeNode]) -> str:
        if root is None:
            return ''
        if root.left is None and root.right is None:
            return str(root.val)
        leftStr = self.tree2str(root.left)
        rightStr = self.tree2str(root.right)
        if leftStr and rightStr == '':
            return str(root.val) + '(' + leftStr + ')'
        if leftStr == '' and rightStr:
            return str(root.val) + '()' + '(' + rightStr + ')'
        return str(root.val) + '(' + leftStr + ')' + '(' + rightStr + ')'



