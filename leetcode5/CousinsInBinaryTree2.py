# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

parentX = None
parentY = None
depthX = 0
depthY = 0
valX = 0
valY = 0
class Solution:
    def __init__(self):
        global parentX
        global parentY
        global depthX
        global depthY
        global valX
        global valY
        parentX = None
        parentY = None
        depthX = 0
        depthY = 0
        valX = 0
        valY = 0

    def isCousins(self, root: [TreeNode], x: int, y: int) -> bool:
        global valX
        global valY
        valX = x
        valY = y
        self.traverse(root, 0, None)
        if depthX == depthY and parentX != parentY:
            return True
        else:
            return False

    def traverse(self, root, depth, parent):
        if root is None:
            return
        global parentX
        global parentY
        global depthX
        global depthY
        if root.val == valX:
            depthX = depth
            parentX = parent
        if root.val == valY:
            depthY = depth
            parentY = parent
        self.traverse(root.left, depth+1, root)
        self.traverse(root.right, depth+1, root)
