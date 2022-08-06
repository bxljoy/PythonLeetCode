# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: [TreeNode]) -> [[int]]:
        res = []
        if root is None:
            return res
        queue = []
        queue.append(root)
        flag = True
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if flag:
                    level.append(cur.val)
                else:
                    level.insert(0, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
            if flag:
                flag = False
            else:
                flag = True
        return res


