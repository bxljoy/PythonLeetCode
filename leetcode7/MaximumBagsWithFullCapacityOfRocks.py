class Solution:
    def maximumBags(self, capacity: [int], rocks: [int], additionalRocks: int) -> int:
        res = 0
        diff = []
        for i in range(len(capacity)):
            diff.append(capacity[i] - rocks[i])
        diff.sort()
        for i in range(len(diff)):
            additionalRocks -= diff[i]
            if additionalRocks > 0:
                res += 1
            elif additionalRocks == 0:
                res += 1
                break
            else:
                break
        return res


