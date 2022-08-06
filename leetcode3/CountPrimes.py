import math

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = []
        for _ in range(n):
            isPrimes.append(True)
        for i in range(2, int(math.sqrt(n))+1):
            if isPrimes[i]:
                for j in range(i*i, n, i):
                    isPrimes[j] = False

        count = 0
        for i in range(2, len(isPrimes)):
            if isPrimes[i]:
                count += 1
        return count

