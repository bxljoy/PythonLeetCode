class Solution:
    def minimumSum(self, num: int) -> int:
        digits = self.getDigits(num)
        return (digits[0]+digits[1])*10 + digits[2] + digits[3]

    def getDigits(self, num):
        array = []
        for _ in range(4):
            array.append(num % 10)
            num = num // 10
        array.sort()
        return array

if __name__ == '__main__':
    s = Solution()
    print(s.minimumSum(2932))
