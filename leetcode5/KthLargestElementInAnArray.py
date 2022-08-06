from heapq import heapify, heappop, heappush
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        res = []
        heapify(res)
        for num in nums:
            heappush(res, num)
            while len(res) > k:
                heappop(res)
        return res[0]




