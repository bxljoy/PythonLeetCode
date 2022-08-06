"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

res = 0
depth = 0
class Solution:
    def __init__(self):
        global res
        global depth
        res = 0
        depth = 0

    def maxDepth(self, root: 'Node') -> int:
        self.traverse(root)
        return res

    def traverse(self, root):
        if root is None:
            return
        global depth
        global res
        depth += 1
        res = max(res, depth)
        for child in root.children:
            self.traverse(child)
        depth -= 1

class Solution1:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        res = 0
        for child in root.children:
            childDepth = self.maxDepth(child)
            res = max(res, childDepth)
        return res + 1


