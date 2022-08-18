class Solution:
    def minSetSize(self, arr: [int]) -> int:
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]] = dic.setdefault(arr[i], 0) + 1
        nums = list(dic.values())
        nums.sort(reverse=True)
        res = 0
        size = len(arr)
        while size > len(arr)//2:
            size -= nums[res]
            res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    arr = [3,3,3,3,5,5,5,2,2,7]
    s.minSetSize(arr)
