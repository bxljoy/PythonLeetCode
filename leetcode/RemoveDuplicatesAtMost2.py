class Solution:
    def removeDuplicates(self, nums):
        for num in nums:
            count = nums.count(num)
            if count > 2:
                for _ in range(count - 2):
                    nums.remove(num)
        return len(nums)

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    k = s.removeDuplicates(nums)
    print(k)
    print(nums)
