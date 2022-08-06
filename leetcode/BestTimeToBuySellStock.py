class Solution2:
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if (prices[j] - prices[i]) > maxProfit:
                    maxProfit = prices[j] - prices[i]
        return maxProfit

class Solution1:
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    if (prices[j] - prices[i]) > maxProfit:
                        maxProfit = prices[j] - prices[i]
        return maxProfit

class Solution:
    def maxProfit(self, prices):
        pass

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution1()
    print(s.maxProfit(prices))
