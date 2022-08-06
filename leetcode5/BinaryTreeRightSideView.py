# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        res = []
        if root is None:
            return res
        queue = []
        queue.append(root)
        while len(queue) > 0:
            last = queue[-1]
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(last.val)
        return res

res = []
depth = 0
class Solution:
    def __init__(self):
        global res
        global depth
        res = []
        depth = 0

    def rightSideView(self, root: [TreeNode]) -> [int]:
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global res
        global depth
        depth += 1
        if len(res) < depth:
            res.append(root.val)
        self.traverse(root.right)
        self.traverse(root.left)
        depth -= 1
