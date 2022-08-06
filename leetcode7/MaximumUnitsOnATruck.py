class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        '''
            dic: units Number as key, boxType as value
        '''
        dic = {}
        res = 0
        for i in range(len(boxTypes)):
            v = dic.setdefault(boxTypes[i][1], 0)
            dic[boxTypes[i][1]] = v + boxTypes[i][0]
        unitsNum = list(dic.keys())
        unitsNum.sort(reverse=True)
        remain = truckSize
        for i in range(len(unitsNum)):
            boxNum = dic[unitsNum[i]]
            remain -= boxNum
            if remain > 0:
                res += unitsNum[i] * boxNum
            elif remain == 0:
                res += unitsNum[i] * boxNum
                break
            else:
                res += (remain + boxNum) * unitsNum[i]
                break
        return res

