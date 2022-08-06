builder = []
class Codec:
    def __init__(self):
        global builder
        builder = []

    def serialize(self, root):
        if root is None:
            return '#'
        global builder
        self.traverse(root)
        return ''.join(builder)

    def traverse(self, root):
        if root is None:
            builder.append('#')
            builder.append(',')
            return
        builder.append(str(root.val))
        builder.append(',')
        self.traverse(root.left)
        self.traverse(root.right)

    def deserialize(self, data):
        if data is None:
            return None
        nodes = data.split(',')
        return self.buildTree(nodes)

    def buildTree(self, nodes):
        if len(nodes) == 0:
            return None
        first = nodes.pop(0)
        if first == '#':
            return None

        root = TreeNode(int(first))
        root.left = self.buildTree(nodes)
        root.right = self.buildTree(nodes)
        return root

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None