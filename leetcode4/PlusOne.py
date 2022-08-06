class Solution:
    def plusOne1(self, digits: [int]) -> [int]:
        sumStr = ''
        for i in digits:
            sumStr = sumStr + str(i)
        res = str(int(sumStr) + 1)
        return list(res)

    def plusOne(self, digits: [int]) -> [int]:
        plus = 1
        res = []
        for i in range(len(digits)-1, -1, -1):
            digits[i] += plus
            if digits[i] == 10:
                if i == 0:
                    digits[i] = 0
                    res.insert(0, 0)
                    res.insert(0, 1)
                else:
                    digits[i] = 0
                    res.insert(0, digits[i])
                    plus = 1
            else:
                plus = 0
                res.insert(0, digits[i])
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 4]
    print(s.plusOne(nums))