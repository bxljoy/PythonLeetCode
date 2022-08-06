import random
from turtle import *

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

def tree(branchLen, t, pensize):
    direct = random.randrange(15, 45)
    randLen1 = random.randrange(12, 15)
    randLen2 = random.randrange(10, 12)
    if branchLen > 5:
        t.pen(pensize=pensize)
        if branchLen < 12:
            t.color('green')
        t.forward(branchLen)
        t.right(direct)
        tree(branchLen-randLen1, t, pensize-1)
        if branchLen < 12:
            t.color('green')
        else:
            t.color('brown')
        t.left(direct*2)
        tree(branchLen-randLen2, t, pensize-1)
        t.right(direct)
        t.backward(branchLen)


if __name__ == '__main__':
    t = Turtle()
    t.shape('circle')
    # drawSpiral(t, 100)
    # t.exitonclick()

    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color('brown')
    t.pen(speed=10)
    t.pen(pensize=10)
    tree(110, t, 10)
    t.exitonclick()


