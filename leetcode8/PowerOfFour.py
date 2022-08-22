class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 4 == 0:
            if n // 4 == 1:
                return True
            else:
                return self.isPowerOfFour(n // 4)
        else:
            return False