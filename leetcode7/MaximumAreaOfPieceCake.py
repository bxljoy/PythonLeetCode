class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: [int], verticalCuts: [int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort(reverse=True)
        maxHorizon = 0
        for i in range(len(horizontalCuts)-1):
            maxHorizon = max(maxHorizon, horizontalCuts[i] - horizontalCuts[i+1])
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort(reverse=True)
        maxVertical = 0
        for i in range(len(verticalCuts)-1):
            maxVertical = max(maxVertical, verticalCuts[i] - verticalCuts[i+1])
        return (maxVertical * maxHorizon) % (10**9 + 7)

