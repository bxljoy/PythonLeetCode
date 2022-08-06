class MinBinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return self.currentSize

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def percDown(self, i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        firstNode = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return firstNode

    def findMin(self):
        if not self.isEmpty():
           return self.heapList[1]

    def buildHeap(self, list):
        for i in list:
            self.insert(i)

    def buildHeap2(self, list):
        i = len(list) // 2
        self.currentSize = len(list)
        self.heapList = [0] + list[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

if __name__ == '__main__':
    array = [9, 6, 5, 2, 3, 7, 4, 10]
    bh2 = MinBinaryHeap()
    bh2.buildHeap2(array)
    print(bh2.heapList)
