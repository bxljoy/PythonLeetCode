class Solution:
    def wordSubsets(self, words1: [str], words2: [str]) -> [str]:
        res = []
        dic = {}
        for word2 in words2:
            for i in range(len(word2)):
                value = dic.setdefault(word2[i], 0)
                dic[word2[i]] = max(value, word2.count(word2[i]))
        for word1 in words1:
            flag = True
            for k, v in dic.items():
                if k not in word1:
                    flag = False
                    break
                else:
                    if word1.count(k) < v:
                        flag = False
                        break
            if flag:
                res.append(word1)
        return res



