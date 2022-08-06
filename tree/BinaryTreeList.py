"""
use List to implement BinaryTree
"""
def BianryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    left = root.pop(1)
    if len(left) > 1:
        root.insert(1, [newBranch, left, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    right = root.pop(2)
    if len(right) > 1:
        root.insert(2, [newBranch, [], right])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newval):
    root[0] = newval

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    r = BianryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    l = getLeftChild(r)
    print(l)
    setRootVal(l, 9)
    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))

