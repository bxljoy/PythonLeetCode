class Solution:
    def isPalindrome(self, x):
        xStr = str(x)
        array = list(xStr)
        array.reverse()
        yStr = ''.join(array)
        if xStr == yStr:
            return True
        else:
            return False




if __name__ == '__main__':
    '''
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
    Therefore it is not a palindrome.
    '''
    x = 121
    s = Solution()
    print(s.isPalindrome(x))
