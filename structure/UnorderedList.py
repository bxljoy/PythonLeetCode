
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, target):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == target:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            if found:
                previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
        if previous == None:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(Node(item))

    def index(self, item):
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        if not found:
            count = -1
        return count

    def insert(self, pos, item):
        current = self.head
        previous = None
        count = 0
        found = False
        while current != None and not found:
            if count == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        if previous == None:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)

    def poplast(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
            return current.getData()
        else:
            previous.setNext(None)
        return current.getData()

    def pop(self, pos):
        current = self.head
        previous = None
        count = 0
        found = False
        while current != None and not found:
            if count == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
                count += 1
        if previous == None:
            self.head = current.getNext()
            return current.getData()
        else:
            previous.setNext(current.getNext())
        return current.getData()

    def slice(self, start, stop):
        current = self.head
        pos = 0
        newList = []
        while current != None and pos < stop:
            if pos >= start:
                data = current.getData()
                newList.append(data)
            current = current.getNext()
            pos = pos + 1
        return newList

    def peek(self):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        topData = current.getData()
        return topData

    def __str__(self):
        current = self.head
        unList = []
        while current != None:
            unList.append(str(current.getData()))
            current = current.getNext()
        unString = '[' + ', '.join(unList) + ']'
        return unString

if __name__ == '__main__':
    un = UnorderedList()
    print(un.isEmpty())
    print(un.length())
    un.append(123)
    un.add(31)
    un.add(77)
    un.add(17)
    un.add(93)
    un.add(26)
    un.add(54)
    print(un.isEmpty())
    print(un.length())
    print(un)
    un.append(44)
    print(un)
    un.remove(32)
    print(un)
    print(un.slice(0, 3))
    print(un.index(17))
    print(un.search(77))
    un.insert(3, 55)
    print(un)
    print(un.pop(0))
    print(un)
    print(un.pop(3))
    print(un)
    print(un.pop(4))
    print(un)
    print(un.poplast())
    print(un)
    print(un.peek())


