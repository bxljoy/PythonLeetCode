class Solution:
    def maxScore(self, cardPoints: [int], k: int) -> int:
        n = len(cardPoints)
        left = 0
        right = n - k
        currentSum = sum(cardPoints[n - k:])
        maxSum = currentSum
        while left < n - k:
            currentSum += cardPoints[left]
            currentSum -= cardPoints[right]
            left += 1
            right -= 1
            maxSum = max(maxSum, currentSum)
        return maxSum
