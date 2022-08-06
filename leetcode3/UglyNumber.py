class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n == 2 or n == 3 or n == 5:
                break
            if n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False
        return True

