class Solution:
    def reverseWords(self, sentence):
        left = 0
        right = len(sentence) - 1
        s = list(sentence)
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords('hello world dora'))
