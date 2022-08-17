class Solution:
    def secondHighest(self, s: str):
        res = set()
        for i in range(len(s)):
            if s[i].isdigit():
                res.add(int(s[i]))
        nums = list(res)
        nums.sort()
        if len(nums) < 2:
            return -1
        else:
            return nums[-2]


