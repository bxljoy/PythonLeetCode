"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
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
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            res.append(array)
        return res

