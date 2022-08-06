class Solution:
    def longestWord(self, words: [str]) -> str:
        dic = {}
        words.sort()
        print(words)
        start = ''
        res = ''
        for i in range(len(words)):
            if res == '':
                if len(words[i]) == 1:
                    start = words[i]
                    res = words[i]
                    dic[start] = res
                continue
            if len(res) + 1 == len(words[i]):
                if words[i].find(res) == 0:
                    res = words[i]
                    dic[start] = res
            else:
                if len(words[i]) == 1:
                    start = words[i]
                    res = words[i]
                    dic[start] = res
                elif len(words[i]) == 2:
                    if words[i][0] in dic:
                        start = i
                        res = words[i]
                        dic[start] = res
        print(dic)
        res = ''
        for value in dic.values():
            if len(res) < len(value):
                res = value
            elif len(res) == len(value):
                res = self.getLexicoOrder(res, value)
        return res

    def getLexicoOrder(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                return s1
            elif s1[i] > s2[i]:
                return s2
        return s1

if __name__ == '__main__':
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    words1 = ["m", "mo", "moc", "moch", "mocha", "l", "la", "lat", "latt", "latte", "c", "ca", "cat"]
    words2 = ["m", "ma", "mat", "math", "s", "sc", "sci", "scie", "scien", "scienc", "science", "a", "ar", "art"]
    words3 = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    words4 = ["ogz", "eyj", "e", "ey", "hmn", "v", "hm", "ogznkb", "ogzn", "hmnm", "eyjuo", "vuq", "ogznk", "og", "eyjuoi", "d"]
    words5 = ["rac", "rs", "ra", "on", "r", "otif", "o", "onpdu", "rsf", "rs", "ot", "oti", "racy", "onpd"]
    s = Solution()
    print(s.longestWord(words5))
