class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # exchange from left up to right down
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # reverse line by line
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                tmp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = tmp
                left += 1
                right -= 1



