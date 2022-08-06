class Solution:
    def leftBound(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1

    def leftBound1(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 2, 3]
    target = 2
    print(s.leftBound(nums, target))