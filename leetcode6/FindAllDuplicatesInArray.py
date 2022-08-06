class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        res = []
        frequent = {}
        for num in nums:
            value = frequent.setdefault(num, 0)
            frequent[num] = value + 1
        for k, v in frequent.items():
            if v == 2:
                res.append(k)
        return res