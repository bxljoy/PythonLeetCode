class Solution:
    def isNStraightHand(self, hand: [int], groupSize: int) -> bool:
        length = len(hand)
        if length % groupSize != 0:
            return False
        n = length // groupSize
        for j in range(n):
            minVal = min(hand)
            hand.remove(minVal)
            for i in range(1, groupSize):
                value = minVal + i
                if value in hand:
                    hand.remove(value)
                else:
                    return False
        return True

