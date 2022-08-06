class Solution:
    def removeDuplicates(self, nums):
        for num in nums:
            count = nums.count(num)
            if count > 1:
                for _ in range(count - 1):
                    nums.remove(num)
        return len(nums)

class Solution1:
    def removeDuplicates(self, nums):
        first = 0
        second = 0
        while second < len(nums):
            if nums[first] == nums[second]:
                second += 1
                continue
            else:
                first += 1
                nums[first] = nums[second]
                second += 1
        return first+1

class Solution2:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                count += 1
                nums[count] = nums[i]
        return count+1

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # s = Solution()
    # k = s.removeDuplicates(nums)
    # print(k)
    # print(nums)

    # s1 = Solution1()
    # k1 = s1.removeDuplicates(nums)
    # print(k1)
    # print(nums)

    s2 = Solution2()
    k2 = s2.removeDuplicates(nums)
    print(k2)
    print(nums)