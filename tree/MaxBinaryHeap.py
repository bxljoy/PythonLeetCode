class MaxBinaryHeap:
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
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[mc] > self.heapList[i]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def findMax(self):
        if not self.isEmpty():
            return self.heapList[1]

    def delMax(self):
        maxNode = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return maxNode

    def buildHeap1(self, aList):
        for i in aList:
            self.insert(i)

    def buildHeap2(self, aList):
        i = len(aList) // 2
        self.currentSize = len(aList)
        self.heapList = [0] + aList[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

if __name__ == '__main__':
    array = [2, 3, 5, 6, 9]
    heap = MaxBinaryHeap()
    heap.buildHeap1(array)
    print(heap.heapList)

    array2 = [2, 3, 5, 6, 9]
    heap2 = MaxBinaryHeap()
    heap2.buildHeap2(array2)
    print(heap2.heapList)

