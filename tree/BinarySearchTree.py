class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
                self.size += 1
        elif key == currentNode.key:
            currentNode.payload = val
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)
                self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.hasRightChild():
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot:
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
            self.rotateRight(node)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # 没有子节点，也就是叶子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
                self.updateBalanceDelete(currentNode.parent)
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.balanceFactor += 1
                self.updateBalanceDelete(currentNode.parent)
        elif currentNode.hasBothChildren():  # 有两个子节点 : 需要寻找后继节点，后继节点就是右子树中的最小节点，必然是叶子节点
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            # self.spliceOut(succ)
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # 只有一个子节点
            if currentNode.hasLeftChild():  # 只有左子节点
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.parent.balanceFactor -= 1
                    self.updateBalanceDelete(currentNode.parent)
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.balanceFactor += 1
                    self.updateBalanceDelete(currentNode.parent)
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:  # 只有右子节点
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.parent.balanceFactor -= 1
                    self.updateBalanceDelete(currentNode.parent)
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.balanceFactor += 1
                    self.updateBalanceDelete(currentNode.parent)
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

    def updateBalanceDelete(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return

        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor -= 1
            elif node.isRightChild():
                node.parent.balanceFactor += 1

            self.updateBalanceDelete(node.parent)

    def spliceOut(self, node):
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild = None
                node.parent.balanceFactor -= 1
            else:
                node.parent.rightChild = None
                node.parent.balanceFactor += 1
        elif node.hasAnyChildren():
            if node.isLeftChild():
                if node.hasLeftChild():
                    node.leftChild.parent = node.parent
                    node.parent.leftChild = node.leftChild
                else:
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
            else:
                if node.hasLeftChild():
                    node.leftChild.parent = node.parent
                    node.parent.rightChild = node.leftChild
                else:
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild

    def inorderTraversal(self):
        '''
            use findSuccessor() to implment a un-recursion middle order traversal
        '''
        res = []
        succ = self.root.findMin()
        res.append(succ)
        while succ:
            succ = succ.findSuccessor()
            if succ:
                res.append(succ)
        return res

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None, balanceFactor=0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = balanceFactor

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.hasLeftChild() or self.hasRightChild())

    def hasAnyChildren(self):
        return self.hasLeftChild() or self.hasRightChild()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def replaceNodeData(self, key, value, lc, rc, balanceFactor=0):
        self.key = key
        self.payload = value
        self.balanceFactor = balanceFactor
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
                self.parent.balanceFactor -= 1
            else:
                self.parent.rightChild = None
                self.parent.balanceFactor += 1
        elif self.hasAnyChildren():
            if self.isLeftChild():
                if self.hasLeftChild():
                    self.leftChild.parent = self.parent
                    self.parent.leftChild = self.leftChild
                else:
                    self.rightChild.parent = self.parent
                    self.parent.leftChild = self.rightChild
            else:
                if self.hasLeftChild():
                    self.leftChild.parent = self.parent
                    self.parent.rightChild = self.leftChild
                else:
                    self.rightChild.parent = self.parent
                    self.parent.rightChild = self.rightChild

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put(1, 1)
    bst.put(2, 2)
    bst.put(3, 3)
    bst.put(4, 4)
    bst.put(5, 5)
    bst.put(6, 6)
    bst.put(7, 6)
    bst.put(8, 6)
    bst.put(9, 7)
    bst.put(10, 9)
    bst.put(11, 8)
    bst.delete(8)
    for elem in bst:
        print(elem)


