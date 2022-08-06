class Solution:
    def minDeletion(self, nums: [int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            if i % 2 == 0 and nums[i] == nums[i+1]:
                nums.remove(nums[i])
                res += 1
                i -= 1

        if len(nums) % 2 == 0:
            return res
        else:
            return res+1