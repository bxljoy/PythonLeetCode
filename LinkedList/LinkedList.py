class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '<Node : %s>' % self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next
        return count

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def search(self, key):
        current = self.head
        found = False
        while current and not found:
            if current.data == key:
                found = True
            else:
                current = current.next
        return found

    def append(self, item):
        """
        add a new node in the tail of the list
        :param item:
        :return:
        """
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert(self, index, item):
        """
        insert a new node in the position index of the linked list
        :param index: the node's index in the linked list
        :param item: the data that contained in the node
        :return: no return value
        """
        if index <= 0:
            self.add(item)
        elif index > self.size()-1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.head
            position = 0
            while position < index-1:
                pre = pre.next
                position += 1
            node.next = pre.next
            pre.next = node

    def node_at_index(self, index):
        """
        get the index position node in the linked list
        :param index: the index number(start from 0)
        :return: the node of index in the linked list
        """
        if index == 0:
            return self.head

        current = self.head
        position = 0
        while position < index:
            current = current.next

        return current

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next

        return '--> '.join(nodes)


if __name__ == '__main__':
    node = Node(1)
    print(node)
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    print(l)
    l.append(6)
    print(l)
    l.insert(5, 100)
    print(l)
