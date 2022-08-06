class Solution:
    def largeGroupPositions(self, s: str) -> [[int]]:
        res = []
        left = 0
        right = 1
        while right < len(s):
            if s[left] != s[right]:
                if right - left >= 3:
                    res.append([left, right-1])
                left = right
            right += 1
        return res


