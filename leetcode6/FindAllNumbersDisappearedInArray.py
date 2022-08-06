class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        set1 = {i for i in range(1, len(nums)+1)}
        set2 = set(nums)
        return list(set1.difference(set2))

