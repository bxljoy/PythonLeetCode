
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        if length < 2:
            return None
        hash_map = dict()
        for i in range(length):
            hash_map[nums[i]] = i
        for i in range(length):
            res = target - nums[i]
            if res in nums[i+1:]:
                return [i, hash_map.get(res)]

if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
