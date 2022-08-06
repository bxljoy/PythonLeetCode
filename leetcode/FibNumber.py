class Solution1:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        numberStore = dict()
        numberStore[0] = 0
        numberStore[1] = 1
        for i in range(2, n+1):
            numberStore[i] = numberStore[i-1] + numberStore[i-2]
        return numberStore[n]

