# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: [TreeNode], x: int, y: int) -> bool:
        res = {}
        queue = []
        queue.append(root)
        depth = 0
        res[root.val] = [depth, None]
        while len(queue) > 0:
            depth += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                    res[cur.left.val] = [depth, cur]
                if cur.right:
                    queue.append(cur.right)
                    res[cur.right.val] = [depth, cur]
        if res[x][0] == res[y][0] and res[x][1] != res[y][1]:
            return True
        else:
            return False
