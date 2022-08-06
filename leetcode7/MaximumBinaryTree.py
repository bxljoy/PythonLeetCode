# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> [TreeNode]:
        if len(nums) == 0:
            return None
        maxVal = max(nums)
        indexMaxVal = nums.index(maxVal)
        root = TreeNode(maxVal)

        root.left = self.constructMaximumBinaryTree(nums[:indexMaxVal])
        root.right = self.constructMaximumBinaryTree(nums[indexMaxVal+1:])
        return root





