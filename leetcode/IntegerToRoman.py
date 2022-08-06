class Solution1:
    def intToRoman(self, num):
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        res = splitNum(num, [])
        result = ""
        for j in range(len(res)):
            result = result + roman[res[j]]
        return result

def splitNum(num, res):
    keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    if num == 0:
       return res
    for i in range(len(keys)):
        if num >= keys[i]:
            res.append(keys[i])
            return splitNum(num - keys[i], res)

class Solution2:
    def __init__(self):
        self.res = []
    def intToRoman(self, num):
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        for i in range(len(keys)):
            if num >= keys[i]:
                self.res.append(keys[i])
                return self.intToRoman(num - keys[i])

        result = ""
        if num == 0:
            for j in range(len(self.res)):
                result = result + roman[self.res[j]]
        return result

class Solution:
    def intToRoman(self, num):
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
                 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""
        while num > 0:
            newKeys = [k for k in keys if k <= num]
            if len(newKeys) == 0:
                break
            num -= newKeys[0]
            result = result + roman[newKeys[0]]

        return result

if __name__ == '__main__':
    '''
    Input: num = 3
    Output: "III"
    Explanation: 3 is represented as 3 ones.
    
    Input: num = 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.

    Input: num = 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    '''
    num = 1994
    s = Solution()
    print(s.intToRoman(3))
    s = Solution()
    print(s.intToRoman(58))
    s = Solution()
    print(s.intToRoman(num))
