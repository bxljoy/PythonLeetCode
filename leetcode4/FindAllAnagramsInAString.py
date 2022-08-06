class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        res = []
        window = {}
        need = {}
        for i in range(len(p)):
            pv = need.setdefault(p[i], 0)
            need[p[i]] = pv + 1
        left = 0
        right = 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                cw = window.setdefault(c, 0)
                window[c] = cw + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if (right - left) == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    dw = window.setdefault(d, 0)
                    window[d] = dw - 1
        return res


