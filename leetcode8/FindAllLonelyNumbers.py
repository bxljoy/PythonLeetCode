class Solution:
    def findLonely(self, nums):
        if len(nums) == 1:
            return nums
        nums.sort()
        res = []
        slow = 0
        fast = 1
        pre = -2
        while fast < len(nums):
            if pre+1 < nums[slow] and nums[slow]+1 < nums[fast]:
                res.append(nums[slow])
            pre = nums[slow]
            slow = fast
            fast += 1

        if pre+1 < nums[slow]:
            res.append(nums[slow])
        return res

