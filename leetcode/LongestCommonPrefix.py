class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        res = ""
        shortStr = strs[0]
        length = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < length:
                shortStr = strs[i]
                length = len(shortStr)
        for i in range(length):
            match = True
            for j in range(len(strs)):
                if shortStr[i] != strs[j][i]:
                    match = False
            if match:
                res += shortStr[i]
            else:
                return res
        return res

if __name__ == '__main__':
    '''
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    '''
    strs = ["flower", "flow", "flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
