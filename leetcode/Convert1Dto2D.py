class Solution:
    def construct2DArray(self, original, m, n):
        """
        Input: mat = [1,2,3,4], r = 1, c = 4
        Output: [[1,2,3,4]]
        """
        count = len(original)
        if count != m * n:
            return []
        else:
            result = []
            for i in range(m):
                result.append(original[i*n:i*n+n])
            return result

if __name__ == '__main__':
    mat = [1, 2, 3, 4]
    r = 1
    c = 4
    s = Solution()
    print(s.construct2DArray(mat, r, c))
