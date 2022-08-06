import UnorderedList as ul

class Deque:
    def __init__(self):
        self.items = ul.UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.length()

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(self.items.length() - 1)

    def addRear(self, item):
        self.items.add(item)

    def removeRear(self):
        return self.items.pop(0)

def palChecker(aString):
    pal = True
    deq = Deque()
    aString = aString.replace(' ', '')
    for a in aString:
        deq.addFront(a)
    while deq.size() > 1:
        front = deq.removeFront()
        rear = deq.removeRear()
        if front != rear:
            pal = False
            break
    return pal

if __name__ == '__main__':
    print(palChecker(' ma    dd am '))