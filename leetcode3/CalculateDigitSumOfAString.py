class Solution:
    def digitSum(self, s: str, k: int) -> str:
        length = len(s)
        if length <= k:
            return s
        digit = ''
        t = length // k
        for i in range(t):
            sub = s[i*k:(i+1)*k]
            digit = digit + str(self.getDigitSum(int(sub)))
        if s[t*k:] != '':
            digit = digit + str(self.getDigitSum(int(s[t*k:])))
        return self.digitSum(digit, k)

    def getDigitSum(self, num):
        if num < 10:
            return num
        return self.getDigitSum(num // 10) + (num % 10)

if __name__ == '__main__':
    s = Solution()
    s.digitSum("11111222223", 3)

