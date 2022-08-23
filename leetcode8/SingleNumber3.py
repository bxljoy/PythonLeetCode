class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        res = []
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.setdefault(num, 0)
        for k,v in dic.items():
            if v == 1:
                res.append(k)
        return res
