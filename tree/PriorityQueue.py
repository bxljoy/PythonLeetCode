from MinBianryHeap import MinBinaryHeap

class PriorityQueue:
    def __init__(self):
        self.minHeap = MinBinaryHeap()

    def enqueue(self, element):
        self.minHeap.insert(element)

    def dequeue(self):
        return self.minHeap.delMin()

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(10)
    pq.enqueue(1)
    pq.enqueue(15)
    pq.enqueue(4)
    pq.enqueue(3)
    pq.enqueue(8)
    pq.enqueue(9)
    pq.enqueue(6)
    pq.enqueue(13)

    while pq.minHeap.size() > 0:
        print(pq.dequeue())

