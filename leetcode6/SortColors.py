class Solution:
    def sortColors(self, nums: [int]) -> None:
        for j in range(len(nums)-1, 0, -1):
            for i in range(j):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        """
        Do not return anything, modify nums in-place instead.
        """