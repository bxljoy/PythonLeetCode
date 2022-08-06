
class Solution1:
    def threeSum(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1 and (0 in nums):
            return []

        res = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                num = 0 - nums[i] - nums[j]
                if num in nums[j+1:length]:
                    array = [nums[i], nums[j], num]
                    if array not in res:
                        res.append(array)
        return res


class Solution:
    def threeSum(self, nums):
        if nums == [] or nums == [0]:
            return []

        res = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        array = [nums[i], nums[j], nums[k]]
                        if array not in res:
                            res.append(array)
        return res

if __name__ == '__main__':
    '''
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    '''
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
