class Solution:
    def reverse(self, x: int) -> int:
        array = list(str(x))
        left = 0
        if array[0] == '-':
            left += 1
        right = len(array) - 1
        while left < right:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            left += 1
            right -= 1
        res = int(''.join(array))
        if res > 2147483647 or res < -2147483646:
            return 0
        else:
            return res

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-1234))
    print(2**31-1)
