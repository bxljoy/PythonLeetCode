import random
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class QueueBack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

def passPotato(names):
    num = random.randint(1, 10)
    q = Queue()
    count = 0
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        head = q.dequeue()
        q.enqueue(head)
        count += 1
        if count == num:
            count = 0
            q.dequeue()
    return q.dequeue()

if __name__ == '__main__':
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    name1, name2, name3, name4, name5, name6 = names
    print(name1)
    print(name3)
    print(name6)
    print(passPotato(names))
    print(passPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"]))