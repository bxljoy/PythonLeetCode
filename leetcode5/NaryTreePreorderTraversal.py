"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

res = []
class Solution:
    def __init__(self):
        global res
        res = []

    def preorder(self, root: 'Node') -> [int]:
        if root is None:
            return res
        res.append(root.val)
        for child in root.children:
            self.preorder(child)
        return res