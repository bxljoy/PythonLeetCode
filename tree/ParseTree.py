import operator

from tree.BinaryTree import BinaryTree
from structure.StackStudy import Stack

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            parent = pStack.pop()
            currentTree = parent
        else:
            raise ValueError('Unknown Operator: ', i)
    return eTree

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()

    if left and right:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parseTree.getRootVal()

def postordereval(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = None
    right = None

    if parseTree:
        left = postordereval(parseTree.getLeftChild())
        right = postordereval(parseTree.getRightChild())

        if left and right:
            return opers[parseTree.getRootVal()](left, right)
        else:
            return parseTree.getRootVal()

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def printexp(tree):
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

if __name__ == '__main__':
    fp = '( 3 + ( 4 * 5 ) )'
    pt = buildParseTree(fp)
    print(evaluate(pt))
    print(postordereval(pt))

    pt2 = BinaryTree('+')
    pt2.insertLeft('3')
    pt2.insertRight('*')
    right = pt2.getRightChild()
    right.insertLeft('4')
    right.insertRight('5')
    print(printexp(pt2))
