class Solution:
    def diStringMatch(self, s: str) -> [int]:
        n = len(s) + 1
        nums = range(n)
        left = 0
        right = n - 1
        res = []
        for i in range(len(s)):
            if s[i] == 'I':
                res.append(nums[left])
                left += 1
            else:
                res.append(nums[right])
                right -= 1
        res.append(nums[left])
        return res
