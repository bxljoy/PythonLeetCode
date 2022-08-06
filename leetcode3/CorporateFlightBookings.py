class Solution:
    def corpFlightBookings(self, bookings: [[int]], n: int) -> [int]:
        res = [0] * n
        dif = Difference(res)
        for booking in bookings:
            start = booking[0]
            end = booking[1]
            val = booking[2]
            dif.increment(start-1, end-1, val)
        return dif.result()

class Difference:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(self.diff)):
            self.diff[i] = nums[i] - nums[i-1]

    def increment(self, start, end, val):
        self.diff[start] += val
        if end+1 < len(self.diff):
            self.diff[end+1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(res)):
            res[i] = res[i-1] + self.diff[i]
        return res

if __name__ == '__main__':
    n = 5
    nums = [0] * n
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    dif = Difference(nums)
    for update in updates:
        dif.increment(update[0], update[1], update[2])
    print(dif.result())
    # s = Solution()
    # bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    # n = 5
    # answer = s.corpFlightBookings(bookings, n)
    # print(answer)



