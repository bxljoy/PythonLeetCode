from collections import deque

class Solution1:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s):
        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            d1.update({s[i]: i})
            d2.setdefault(s[i], i)
        print(d1)
        print(d2)
        for j in range(len(s)):
            if d1[s[j]] == d2[s[j]]:
                return d1[s[j]]
        return -1

if __name__ == '__main__':
    target = 'dddccdbba'
    s = Solution2()
    print(s.firstUniqChar(target))
