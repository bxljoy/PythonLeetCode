class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        res = 100001
        for i in range(len(s)):
            v = map.setdefault(s[i], 0)
            map[s[i]] = v + 1
        for k, v in map.items():
            if v == 1:
                res = min(res, s.index(k))
        if res == 100001:
            res = -1
        return res
