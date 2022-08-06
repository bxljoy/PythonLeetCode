from heapq import heapify, heappop, heappush
class KthLargest:
    def __init__(self, k: int, nums: [int]):
        self.res = []
        self.k = k
        heapify(self.res)
        for num in nums:
            heappush(self.res, num)

    def add(self, val: int) -> int:
        heappush(self.res, val)
        while len(self.res) > self.k:
            heappop(self.res)
        return self.res[0]

