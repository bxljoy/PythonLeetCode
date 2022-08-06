class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            print('mid = ' + str(mid))
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[mid] <= target:
            return mid+1
        else:
            return mid

        # low = 0
        # high = len(nums)-1
        # res = 0
        # while low <= high:
        #     mid = (low + high) // 2
        #     print('mid = ' + str(mid))
        #     if nums[mid] == target:
        #         return mid
        #     else:
        #         if mid == 0:
        #             if nums[mid] >= target:
        #                 return mid
        #             else:
        #                 return mid+1
        #         if mid == len(nums)-1:
        #             if nums[len(nums)-1] <= target:
        #                 return len(nums)
        #             else:
        #                 return len(nums)-1
        #         if nums[mid] > target:
        #             high = mid - 1
        #             res = high
        #             print('high = ' + str(high))
        #             print('low = ' + str(low))
        #         else:
        #             low = mid + 1
        #             res = low
        # return res

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    nums1 = [1, 3]
    nums2 = [1, 2, 3, 4, 5, 10]
    target1 = 5
    target2 = 2
    target3 = 0
    target4 = 4
    s = Solution()
    print(s.searchInsert(nums1, target3))
