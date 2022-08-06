class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = []
        for word in words:
            res.append(self.reverse(list(word)))
        return ' '.join(res)

    def reverse(self, s: [str]):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
