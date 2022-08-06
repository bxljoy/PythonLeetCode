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

    def postorder(self, root: 'Node') -> [int]:
        if root is None:
            global res
            return res

        for child in root.children:
            self.postorder(child)
        res.append(root.val)
        return res
