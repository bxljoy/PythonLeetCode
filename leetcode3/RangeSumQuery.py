class NumArray:

    def __init__(self, nums: [int]):
        self.preSum = [0]
        for i in range(1, len(nums)+1):
            self.preSum.append(self.preSum[i-1] + nums[i-1])

    def sumRange(self, left: int, right: int) -> int:
        print(self.preSum)
        return self.preSum[right+1] - self.preSum[left]

    def sumRange2(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum
