class Solution:
    def wiggleSort(self, nums: [int]) -> None:
        nums.sort(reverse=True)
        nums1 = nums[:len(nums)//2]
        nums2 = nums[len(nums)//2:]
        for i in range(1, len(nums), 2):
            nums[i] = nums1[i//2]
        for i in range(0, len(nums), 2):
            nums[i] = nums2[i//2]
        """
        Do not return anything, modify nums in-place instead.
        """
