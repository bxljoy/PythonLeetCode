class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        dic1 = {}
        dic2 = {}
        for i in range(len(list1)):
            dic1[list1[i]] = i
        for i in range(len(list2)):
            dic2[list2[i]] = i
        set1 = set(list1)
        set2 = set(list2)
        set1.intersection_update(set2)
        res = list(set1)
        if len(res) == 1:
            return res
        else:
            resIndex = []
            sum = 0
            for j in range(len(res)):
                indexSum = dic1[res[j]] + dic2[res[j]]
                if j == 0:
                    sum = indexSum
                    resIndex.append(j)
                else:
                    if sum > indexSum:
                        resIndex.clear()
                        resIndex.append(j)
                        sum = indexSum
                    elif sum == indexSum:
                        resIndex.append(j)
            res2 = []
            for index in resIndex:
                res2.append(res[index])
            return res2




