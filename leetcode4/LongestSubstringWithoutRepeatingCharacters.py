class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            cv = window.setdefault(c, 0)
            window[c] = cv + 1
            while window[c] > 1:
                d = s[left]
                left += 1
                dv = window.setdefault(d, 0)
                window[d] = dv - 1
            res = max(res, right - left)
        return res