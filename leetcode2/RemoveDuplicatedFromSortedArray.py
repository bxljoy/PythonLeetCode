class Solution:
    def removeDuplicates2(self, nums: [int]) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                if fast > slow:
                    for i in range(slow+1, fast):
                        nums[i] = nums[fast]
                slow += 1
            fast += 1
        return slow+1

    def removeDuplicates1(self, nums: [int]) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1

    def removeDuplicates(self, nums: [int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1

