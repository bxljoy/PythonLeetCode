from structure import StackStudy as st


class Queue:
    def __init__(self):
        self.stack1 = st.Stack()
        self.stack2 = st.Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeque(self):
        if self.stack1.size() == 0 and self.stack2.size() == 0:
            return []
        elif self.stack2.size() == 0:
            while self.stack1.size() != 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def isEmpty(self):
        if self.stack1.size() == 0 and self.stack2.size() == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    q = Queue()
    q.enqueue(123)
    q.enqueue(456)
    q.enqueue(789)
    print(q.dequeque())
    print(q.dequeque())
    print(q.dequeque())

