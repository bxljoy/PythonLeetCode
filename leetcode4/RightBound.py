class Solution:
    def rightBound(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if left == 0:
            return -1
        if nums[left - 1] == target:
            return left - 1
        else:
            return -1

    def rightBound1(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        return right
