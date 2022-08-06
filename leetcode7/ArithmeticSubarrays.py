class Solution:
    def checkArithmeticSubarrays(self, nums: [int], l: [int], r: [int]) -> [bool]:
        res = []
        for i in range(len(l)):
            res.append(self.isArithmeticSubarrays(nums[l[i]:r[i]+1]))
        return res

    def isArithmeticSubarrays(self, arr):
        if len(arr) < 2:
            return False
        res = True
        arr.sort()
        dif = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if dif != arr[i] - arr[i-1]:
                return False
        return res


