class Solution:
    def buildArray(self, target: [int], n: int) -> [str]:
        res = []
        pointer = 0
        num = 1
        while pointer < len(target):
            res.append('Push')
            if num == target[pointer]:
                pointer += 1
            else:
                res.append('Pop')
            num += 1
        return res

