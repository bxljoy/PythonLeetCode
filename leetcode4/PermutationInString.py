class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        for i in range(len(s1)):
            value = need.setdefault(s1[i], 0)
            need[s1[i]] = value + 1
        left = 0
        right = 0
        length = 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                cv = window.setdefault(c, 0)
                window[c] = cv + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                length = right - left
                if length == len(s1):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    dw = window.setdefault(d, 0)
                    window[d] = dw - 1
        return False

