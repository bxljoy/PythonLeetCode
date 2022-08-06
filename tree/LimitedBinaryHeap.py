class LimitedBinaryHeap:
    def __init__(self, n):
        self.heapList = [0]
        self.currentSize = 0
        self.limit = n

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return self.currentSize

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        while self.currentSize > self.limit:
            self.heapList.pop()
            self.currentSize -= 1

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2

    def delMin(self):
        firstNode = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return firstNode

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def buildHeap(self, aList):
        i = len(aList) // 2
        self.currentSize = len(aList)
        self.heapList = [0] + aList[:]
        while i > 0:
            self.percDown(i)
            i = i - 1
        while self.currentSize > self.limit:
            self.heapList.pop()
            self.currentSize -= 1


if __name__ == '__main__':
    array = [9, 6, 5, 2, 3]
    bh = LimitedBinaryHeap(7)
    bh.buildHeap(array)
    bh.insert(4)
    bh.insert(1)
    bh.insert(4)
    print(bh.heapList)