class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = s + t
        res = 0
        for i in range(len(st)):
            res = res ^ ord(st[i])
        return chr(res)
