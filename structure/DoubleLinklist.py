
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinklist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count = count + 1
        return count

    def add(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        node = Node(item)
        current = self.head
        if self.isEmpty():
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current

    def remove(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
        if found:
            if self.head == current:
                self.head = current.next
                if self.length() > 1:
                    current.next.prev = None

            elif current.next == None:
                current.prev.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

    def search(self, item):
        cur = self.head
        found = False
        while cur != None and not found:
            if cur.item == item:
                found = True
            else:
                cur = cur.next
        return found

    def insert(self, item, pos):
        cur = self.head
        count = 0
        found = False
        node = Node(item)
        while cur != None and not found:
            if pos == count:
                found = True
            else:
                count = count + 1
                cur = cur.next
        if found:
            if pos == 0:
                self.add(item)
            else:
                cur.prev.next = node
                node.next = cur
                node.prev = cur.prev
                cur.prev = node
        else:
            if pos < 0:
                self.add(item)
            if pos >= self.length():
                self.append(item)

    def __str__(self):
        current = self.head
        dLinklist = []
        while current != None:
            dLinklist.append(str(current.item))
            current = current.next
        unString = '[' + ', '.join(dLinklist) + ']'
        return unString

if __name__ == '__main__':
    dLink = DoubleLinklist()
    dLink.append(123)
    dLink.append(456)
    dLink.append(789)
    print(dLink)
    dLink.insert(111, 0)
    print(dLink)
    dLink.insert(222, 2)
    print(dLink)
    dLink.insert(333, -1)
    print(dLink)
    dLink.insert(444, 6)
    print(dLink)
    dLink.insert(555, 100)
    print(dLink)
