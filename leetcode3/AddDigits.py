class Solution:
    def addDigits(self, num: int) -> int:
        while (num >= 10):
            num = self.getDigit(num)
        return num

    def getDigit(self, n):
        if n < 10:
            return n
        return self.getDigit(n//10) + (n%10)

