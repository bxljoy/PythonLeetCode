class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        wMap1 = {}
        wMap2 = {}
        res = 0
        for i in range(len(word1)):
            cv = wMap1.setdefault(word1[i], 0)
            wMap1[word1[i]] = cv + 1
        for i in range(len(word2)):
            cv = wMap2.setdefault(word2[i], 0)
            wMap2[word2[i]] = cv + 1
        for k, v in wMap1.items():
            if k not in wMap2:
                res += wMap1[k]
            else:
                res += abs(v - wMap2[k])
        for k, v in wMap2.items():
            if k not in wMap1:
                res += wMap2[k]
        return res

if __name__ == '__main__':
    s = Solution()
    word1 = "sea"
    word2 = "ate"
    print(s.minDistance(word1, word2))

