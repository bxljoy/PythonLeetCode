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
        if root is None:
            return res
        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            list = []
            for _ in range(size):
                cur = queue.pop(0)
                list.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            res.append(list)
        return res

