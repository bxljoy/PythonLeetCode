class Solution:
    def kthLargestNumber(self, nums: [str], k: int) -> str:
        res = []
        for num in nums:
            res.append(int(num))
        res.sort(reverse=True)
        return str(res[k-1])
    
