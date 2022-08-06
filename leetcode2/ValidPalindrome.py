class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                s1 = s[:left] + s[left+1:]
                s2 = s[:right] + s[right + 1:]
                if self.validPalindrome2(s1) or self.validPalindrome2(s2):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True

    def validPalindrome2(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True



