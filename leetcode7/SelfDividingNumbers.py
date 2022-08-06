class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> [int]:
        res = []
        for i in range(left, right + 1):
            if self.selfDivide(i):
                res.append(i)
        return res

    def selfDivide(self, num):
        res = True
        if num < 10:
            return True
        if num % 10 == 0:
            return False
        tmp = num
        while tmp >= 10:
            if tmp % 10 == 0:
                return False
            divide = tmp % 10
            tmp = tmp // 10
            if num % divide != 0:
                return False
        if num % tmp != 0:
            return False
        return res

if __name__ == '__main__':
    s = Solution()
    left = 66
    right = 708
    print(s.selfDividingNumbers(left, right))
