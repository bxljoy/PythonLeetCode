# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: [TreeNode]) -> int:
        queue = []
        queue.append(root)
        while len(queue) > 0:
            res = 0
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                res += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res

