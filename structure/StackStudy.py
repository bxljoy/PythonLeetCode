
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len[self.items] - 1]

    def size(self):
        return len(self.items)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString):
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(top, symbol):
    opens = '([{'
    closes = ')]}'
    return opens.index(top) == closes.index(symbol)

def divideBy2(num):
    s = Stack()
    while num > 0:
        s.push(num % 2)
        num = num // 2
    binString = ''
    while not s.isEmpty():
        binString += str(s.pop())
    return binString

def baseConventor(num, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while num > 0:
        s.push(num % base)
        num = num // base
    binString = ''
    while not s.isEmpty():
        binString += digits[(s.pop())]
    return binString

if __name__ == '__main__':
    s1 = '(()((())()))'
    s2 = '((((((())'
    print(parChecker(s1))

    print(divideBy2(233))
    print(baseConventor(233, 2))
