# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: [TreeNode]) -> [float]:
        res = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            sum = 0
            for _ in range(size):
                cur = queue.pop(0)
                sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(sum / size)
        return res

