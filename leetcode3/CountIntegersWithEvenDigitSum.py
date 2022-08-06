class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1):
            if i < 10:
                if i % 2 == 0:
                    count += 1
            else:
                digit = self.getDigit(i)
                if (digit % 2 == 0):
                    count += 1
        return count

    def getDigit(self, n):
        if n < 10:
            return n
        return self.getDigit(n//10) + (n%10)