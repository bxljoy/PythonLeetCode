class Solution:
    def maximumUniqueSubarray(self, nums: [int]) -> int:
        window = {}
        left = 0
        right = 0
        sum = 0
        res = 0
        while right < len(nums):
            c = nums[right]
            sum += c
            right += 1
            cv = window.setdefault(c, 0)
            window[c] = cv + 1
            while window[c] > 1:
                d = nums[left]
                sum -= d
                left += 1
                dv = window.setdefault(d, 0)
                window[d] = dv - 1
            res = max(res, sum)
        return res

