class Solution:
    def minimumDeletions(self, nums: [int]) -> int:
        dic = {}
        n = len(nums)
        for i in range(n):
            dic[nums[i]] = i
        keyArr = list(dic.keys())
        keyArr.sort()
        maxIndex = dic[keyArr[n-1]]
        minIndex = dic[keyArr[0]]
        minDeletions = n + 1
        if maxIndex > minIndex:
            first = maxIndex + 1
            minDeletions = min(minDeletions, first)
            second = minIndex + 1 + n - maxIndex
            minDeletions = min(minDeletions, second)
            third = n - minIndex
            minDeletions = min(minDeletions, third)
            return minDeletions
        elif maxIndex < minIndex:
            first = minIndex + 1
            minDeletions = min(minDeletions, first)
            second = maxIndex + 1 + n - minIndex
            minDeletions = min(minDeletions, second)
            third = n - maxIndex
            minDeletions = min(minDeletions, third)
            return minDeletions
        elif maxIndex == minIndex:
            return 1

