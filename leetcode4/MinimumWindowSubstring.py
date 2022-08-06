import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        for i in range(len(t)):
            value = need.setdefault(t[i], 0)
            need[t[i]] = value + 1
        left = 0
        right = 0
        start = 0
        length = sys.maxsize
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
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    dw = window.setdefault(d, 0)
                    window[d] = dw - 1

        if length == sys.maxsize:
            return ""
        else:
            return s[start:start+length]



if __name__ == '__main__':
    s = Solution()
    s.minWindow("ADOBECODEBANC", "ABC")
