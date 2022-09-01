# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.traverse(root, root.val)
        return self.res;

    def traverse(self, root, pathmax):
        if root is None:
            return
        if root.val >= pathmax:
            self.res += 1
            pathmax = root.val
        self.traverse(root.left, pathmax)
        self.traverse(root.right, pathmax)
