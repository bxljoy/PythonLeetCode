class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        dic = {}
        for i in range(len(nums)):
            num = dic.setdefault(nums[i], 0)
            if num == 1:
                return nums[i]
            else:
                dic[nums[i]] = 1



