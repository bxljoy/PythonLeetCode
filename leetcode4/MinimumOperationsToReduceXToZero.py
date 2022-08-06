class Solution:
    def minOperations(self, nums: [int], x: int) -> int:
        nums.sort()
        print(nums)
        left = 0
        right = 0
        sum = 0
        res = -1
        while right < len(nums):
            c = nums[right]
            right += 1
            sum += c
            while sum > x:
                d = nums[left]
                left += 1
                sum -= d
            if sum == x:
                if res == -1:
                    res = right - left
                else:
                    res = min(res, right - left)
        return res


if __name__ == '__main__':
    # nums = [1, 1, 4, 2, 3]
    # x = 5
    # nums = [3, 2, 20, 1, 1, 3]
    # x = 10
    # nums = [1, 1]
    # x = 3
    # nums = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
    # x = 134365
    nums = [6016, 5483, 541, 4325, 8149, 3515, 7865, 2209, 9623, 9763, 4052, 6540, 2123, 2074, 765, 7520, 4941, 5290, 5868,
     6150, 6006, 6077, 2856, 7826, 9119]
    x = 31841
    s = Solution()
    print(s.minOperations(nums, x))
