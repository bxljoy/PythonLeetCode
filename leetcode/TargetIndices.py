class Solution:
    def targetIndices(self, nums, target):
        nums.sort(reverse=False)
        count = nums.count(target)
        result = []
        while count > 0:
            index = nums.index(target)
            result.append(index)
            nums[index] = target+1
            count -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5, 2, 3]
    target = 2
    print(s.targetIndices(nums, target))
