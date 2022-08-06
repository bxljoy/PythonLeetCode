class Solution:
    def repeatedSubstringPattern(self, s):
        length = len(s)
        if length <= 1:
            return False
        result = False
        for i in range(1, length):
            if result:
                break
            count = s.count(s[:i])
            num = int(length / count)
            for i in range(num, length, num):
                if s[i:i+num] != s[i-num:i]:
                    result = False
                    break
                else:
                    result = True
        return result


if __name__ == '__main__':
    '''
    Input: s = "abcabcabcabc"
    Output: true
    Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
    '''
    s = "abcabcabcabc"
    so = Solution()
    print(so.repeatedSubstringPattern(s))

