class Solution:
    def repeatedCharacter(self, s: str):
        dic = {}
        for i in range(len(s)):
            c = s[i]
            count = dic.setdefault(c, 0)
            if count > 0:
                return c
            else:
                dic[c] = count + 1

