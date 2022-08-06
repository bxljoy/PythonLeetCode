import UnorderedList as ul

class Queue:
    def __init__(self):
        self.items = ul.UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.length()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(123)
    q.enqueue(456)
    q.enqueue(789)
    while q.size() != 0:
        print(q.dequeue())