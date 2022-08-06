class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNums = {1, 2, 3, 5}
        while len(uglyNums) < n * 4:
            tmp = []
            for ugly in uglyNums:
                tmp.append(ugly * 2)
                tmp.append(ugly * 3)
                tmp.append(ugly * 5)
            for i in range(len(tmp)):
                uglyNums.add(tmp[i])
        res = list(uglyNums)
        res.sort()
        return res[n-1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(20))
