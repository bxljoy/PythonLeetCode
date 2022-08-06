class Solution:
    def divideString(self, s: str, k: int, fill: str) -> [str]:
        res = []
        element = ''
        for i in range(len(s)):
            if len(element) == k:
                res.append(element)
                element = s[i]
            else:
                element = element + s[i]
        if len(element) > 0:
            while len(element) < k:
                element = element + fill
            res.append(element)
        return res

