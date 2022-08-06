import heapq

# Definition for MinHeap (PriorityQueue)
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def size(self):
        return len(self._queue)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l4 = ListNode(2)
    l3 = ListNode(3)
    pq = PriorityQueue()
    pq.push(l3, l3.val)
    pq.push(l2, l2.val)
    pq.push(l1, l1.val)
    pq.push(l4, l4.val)

    element = pq.pop()
    print(element.val)
    element = pq.pop()
    print(element.val)
    element = pq.pop()
    print(element.val)
    element = pq.pop()
    print(element.val)

