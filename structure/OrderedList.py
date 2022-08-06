
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

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            return None
        elif previous == None:
            self.head = None
            return current.getData()
        else:
            previous.setNext(current.getNext())
            return current.getData()

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        found = False
        stop = False
        count = 0
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData > item:
                    stop = True
                else:
                    current = current.getNext()
                    count += 1
        if not found:
            return None
        else:
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

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        temp.setNext(current)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

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
    un = OrderedList()
    print(un.isEmpty())
    print(un.length())
    un.add(31)
    un.add(77)
    un.add(17)
    un.add(93)
    un.add(26)
    un.add(54)
    print(un.isEmpty())
    print(un.length())
    print(un)
    un.remove(31)
    print(un)
    print(un.index(17))
    print(un.search(77))
    un.insert(3, 55)
    print(un)
    print(un.pop(0))
    print(un)
    print(un.pop(3))
    print(un)
    print(un.pop(3))
    print(un)
    print(un.peek())
