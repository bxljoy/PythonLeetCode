class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        array = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                tmp = s[i:j+1]
                if tmp in array:
                    count += 1
                    continue
                if self.isPalindrome(tmp):
                    count += 1
                    array.append(tmp)
        return count

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings('abc'))
