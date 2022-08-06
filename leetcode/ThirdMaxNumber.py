class Solution:
    def thirdMax(self, nums):
        if len(nums) == 0:
            return None
        nums.sort(reverse=True)
        res = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] < res:
                count += 1
                res = nums[i]
            if count == 2:
                break
        if count < 2:
            res = nums[0]
        return res

class Solution2:
    def thirdMax(self, nums):
        if len(nums) == 0:
            return None
        nums.sort(reverse=True)
        count = 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
            if count == 2:
                res = i
                break
        return nums[res]



if __name__ == '__main__':
    nums = [3, 2, 1]
    nums = [2, 1, 1]
    nums = [3, 2, 2, 1]
    s = Solution()
    print(s.thirdMax(nums))