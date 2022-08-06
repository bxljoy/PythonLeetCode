class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        end = 1
        for i in range(2, len(s)+1):
            if self.isPalindrome(s[:i]):
                end = i
        return self.reverseFromNum(s, end) + s

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def reverseFromNum(self, s, num):
        res = s[:]
        left = num
        right = len(res) - 1
        resList = list(res)
        while left < right:
            resList[left], resList[right] = resList[right], resList[left]
            left += 1
            right -= 1
        res = ''.join(resList)
        return res[num:]

if __name__ == '__main__':
    s = Solution()
    test = "aba"
    print(s.shortestPalindrome(test))
