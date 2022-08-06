# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

maxDiameter = 0
class Solution:
    def __init__(self):
        global maxDiameter
        maxDiameter = 0

    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.maxDepth(root)
        return maxDiameter

    def maxDepth(self, root):
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        myDiameter = leftDepth + rightDepth
        global maxDiameter
        maxDiameter = max(maxDiameter, myDiameter)

        return 1 + max(leftDepth, rightDepth)
