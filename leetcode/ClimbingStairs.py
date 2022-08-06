class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution1:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        stairsTable = dict()
        stairsTable[1] = 1
        stairsTable[2] = 2
        for i in range(3, n+1):
            temp = stairsTable[i-1] + stairsTable[i-2]
            stairsTable[i] = temp
        return stairsTable[n]

if __name__ == '__main__':
    pass