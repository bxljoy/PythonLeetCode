# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: [TreeNode]) -> [[int]]:
            res = []
            queue = []
            if root is None:
                return res
            queue.append(root)
            while len(queue) > 0:
                array = []
                for _ in range(len(queue)):
                    cur = queue.pop(0)
                    array.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                res.insert(0, array)
            return res
