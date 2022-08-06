# remove elments from array
class Solution:
    def removeElement(self, nums, val):
        count = nums.count(val)
        for _ in range(count):
            nums.remove(val)
        return len(nums)

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    s = Solution()
    k = s.removeElement(nums, val)
    print(k)
    print(nums)
