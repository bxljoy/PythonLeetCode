"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)


class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = []
        queue.append(root)
        while len(queue) > 0:
            pre = None
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root


