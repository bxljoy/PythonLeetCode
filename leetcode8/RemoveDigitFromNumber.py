class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index = []
        res = 0
        for i in range(len(number)):
            if number[i] == digit:
                index.append(i)
        for i in range(len(index)):
            if index[i] == 0:
                num = int(number[1:])
            else:
                num = int(number[:index[i]]+number[index[i]+1:])
            res = max(res, num)
        return str(res)


