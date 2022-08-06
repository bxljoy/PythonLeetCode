class Solution:
    def removeAnagrams(self, words: [str]) -> [str]:
        res = words[:]
        for i in range(1, len(words)):
            if self.isAnagram(words[i-1], words[i]):
                res.remove(words[i])
        return res

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        window = {}
        need = {}
        for i in range(len(t)):
            value = need.setdefault(t[i], 0)
            need[t[i]] = value + 1
        point = 0
        valid = 0
        while point < len(s):
            c = s[point]
            point += 1
            if c in need:
                cv = window.setdefault(c, 0)
                window[c] = cv + 1
                if window[c] == need[c]:
                    valid += 1

        if valid == len(need):
            return True
        else:
            return False




