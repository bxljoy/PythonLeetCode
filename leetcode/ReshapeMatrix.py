class Solution:
    def matrixReshape(self, mat, r, c):
        """
        Input: mat = [[1,2],[3,4]], r = 1, c = 4
        Output: [[1,2,3,4]]
        """
        row = len(mat)
        column = len(mat[0])
        if row*column != r*c:
            return mat
        else:
            total = []
            reshapeMatrix = []
            for i in range(row):
                total += mat[i]
            for i in range(r):
                reshapeMatrix.append(total[i*c:i*c+c])
            return reshapeMatrix

if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 4
    c = 1
    s = Solution()
    print(s.matrixReshape(mat, r, c))


