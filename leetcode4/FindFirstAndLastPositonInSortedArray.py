class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums)
        if nums[left] > target or nums[right-1] < target:
            return [-1, -1]
        first = -1
        last = -1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if nums[left] == target:
            first = left

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
        if nums[left - 1] == target:
            last = left - 1

        return [first, last]

