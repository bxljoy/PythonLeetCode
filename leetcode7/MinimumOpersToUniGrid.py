class Solution:
    def minOperations(self, grid: [[int]], x: int) -> int:
        res = 0
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums.append(grid[i][j])
        nums.sort()
        n = len(nums)
        middle = n // 2
        for i in range(n):
            if i < middle:
                diff = nums[middle] - nums[i]
            elif i > middle:
                diff = nums[i] - nums[middle]
            else:
                continue
            if diff % x == 0:
                res += diff // x
            else:
                return -1
        return res


