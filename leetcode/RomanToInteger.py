class Solution1:
    def romanToInt(self, s):
        roman2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        key2 = list(roman2.keys())
        keys = list(roman.keys())
        if s in keys:
            return roman[s]

        res = 0
        for key in key2:
            index = s.find(key)
            if index != -1:
                array = list(s)
                temp = ""
                for i in range(len(array)):
                    if i == index or i == index+1:
                        continue
                    else:
                        temp = temp + array[i]
                s = temp
                res += roman[key]
        restArray = list(s)
        for i in range(len(restArray)):
            res += roman[restArray[i]]
        return res

class Solution2:
    def romanToInt(self, s):
        roman2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        key2 = list(roman2.keys())
        keys = list(roman.keys())
        if s in keys:
            return roman[s]

        res = 0
        for key in key2:
            index = s.find(key)
            temp = ""
            if index != -1:
                if len(s) > index+1:
                    temp = s[0:index] + s[index+2:]
                else:
                    temp = s[0:index]
                s = temp
                res += roman[key]
        restArray = list(s)
        for i in range(len(restArray)):
            res += roman[restArray[i]]
        return res

class Solution3:
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        key2 = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        res = 0
        for key in key2:
            index = s.find(key)
            if index != -1:
                if len(s) > index+1:
                    temp = s[0:index] + s[index+2:]
                else:
                    temp = s[0:index]
                s = temp
                res += roman[key]
        restArray = list(s)
        for i in range(len(restArray)):
            res += roman[restArray[i]]
        return res

class Solution:
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        keys = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        res = 0
        for key in keys:
            index = s.find(key)
            if index != -1:
                if len(s) > index+1:
                    temp = s[0:index] + s[index+2:]
                else:
                    temp = s[0:index]
                s = temp
                res += roman[key]
        for i in range(len(s)):
            res += roman[s[i]]
        return res

if __name__ == '__main__':
    '''
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    
    Input: s = "MCMXCIV"
    Output: 1994
    '''
    str = "MCMXCIV"
    s = Solution()
    print(s.romanToInt(str))
