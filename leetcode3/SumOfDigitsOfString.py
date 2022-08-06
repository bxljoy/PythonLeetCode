class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabets = '0abcdefghijklmnopqrstuvwxyz'
        trans = ''
        for i in range(len(s)):
            trans = trans + str(alphabets.index(s[i]))
        for j in range(k):
            trans = str(self.transform(trans))
        return int(trans)

    def transform(self, digits):
        sum = 0
        for i in range(len(digits)):
            sum += int(digits[i])
        return sum

if __name__ == '__main__':
    s = Solution()
    print(s.getLucky('iiii', 1))
