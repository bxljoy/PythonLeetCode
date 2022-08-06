import UnorderedList as ul

class Stack:
    def __init__(self):
        self.items = ul.UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.length()

    def pop(self):
        return self.items.pop(self.items.length() - 1)

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items.peek()

if __name__ == '__main__':
    s = Stack()
    s.push(123)
    s.push(456)
    s.push(789)
    while s.size() != 0:
        print(s.pop())