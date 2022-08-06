# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> [TreeNode]:
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if postStart > postEnd:
            return None
        rootVal = postorder[postEnd]
        index = inorder.index(rootVal)
        leftSize = index - inStart
        root = TreeNode(rootVal)
        root.left = self.build(inorder, inStart, index-1,
                               postorder, postStart, postStart+leftSize-1)
        root.right = self.build(inorder, index+1, inEnd,
                                postorder, postStart+leftSize, postEnd-1)
        return root

class Solution1:
    def buildTree(self, inorder: [int], postorder: [int]) -> [TreeNode]:
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if postStart > postEnd:
            return None
        rootVal = postorder[postEnd]
        index = inorder.index(rootVal)
        rightSize = inEnd - index
        root = TreeNode(rootVal)
        root.left = self.build(inorder, inStart, index-1,
                               postorder, postStart, postEnd - rightSize - 1)
        root.right = self.build(inorder, index+1, inEnd,
                                postorder, postEnd-rightSize, postEnd-1)
        return root
