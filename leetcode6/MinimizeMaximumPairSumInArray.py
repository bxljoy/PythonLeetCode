class Solution:
    def minPairSum(self, nums: [int]) -> int:
        res = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            res = max(res, nums[left] + nums[right])
            left += 1
            right -= 1
        return res

