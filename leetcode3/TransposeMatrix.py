class Solution:
    def transpose(self, matrix: [[int]]) -> [[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == cols:
            for i in range(rows):
                for j in range(i, cols):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
            return matrix
        else:
            res = [[0] * rows for _ in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    res[j][i] = matrix[i][j]
            return res

if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6]]))
