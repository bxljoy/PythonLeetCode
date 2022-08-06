class Solution:
    def arrayChange(self, nums: [int], operations: [[int]]) -> [int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(operations)):
            index = dic[operations[i][0]]
            nums[index] = operations[i][1]
            dic[operations[i][1]] = index
            dic.pop(operations[i][0])
        return nums
