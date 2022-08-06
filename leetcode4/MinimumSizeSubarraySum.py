class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        left = 0
        right = 0
        sum = 0
        res = 0
        while right < len(nums):
            c = nums[right]
            right += 1
            sum += c
            while sum >= target:
                if res == 0:
                    res = right - left
                else:
                    res = min(res, right - left)
                d = nums[left]
                left += 1
                sum -= d
        return res
