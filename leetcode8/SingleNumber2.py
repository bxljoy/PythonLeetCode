class Solution:
    def singleNumber(self, nums: [int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)

        for k, v in hash_map.items():
            if v == 1:
                return k


