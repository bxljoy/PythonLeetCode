class Solution:
    def wiggleMaxLength(self, nums: [int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        res = 1
        flag = 0
        i = 0
        while i < len(nums):
            diff = nums[i] - nums[i-1]
            if flag == 0:
                flag = diff
                res += 1
            elif flag > 0:
                if diff < 0:
                    res += 1
                    flag = diff
                else:
                    nums.pop(i)
                    i -= 1
            else:
                if diff > 0:
                    res += 1
                    flag = diff
                else:
                    nums.pop(i)
                    i -= 1
            i += 1
        return res



