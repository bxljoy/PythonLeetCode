class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        m = len(matrix)
        n = len(matrix[0])
        upp_bound = 0
        left_bound = 0
        right_bound = n - 1
        low_bound = m - 1
        res = []
        while len(res) < (m * n):
            if upp_bound <= low_bound:
                for i in range(left_bound, right_bound+1):
                    res.append(matrix[upp_bound][i])
                upp_bound += 1
            if left_bound <= right_bound:
                for i in range(upp_bound, low_bound+1):
                    res.append(matrix[i][right_bound])
                right_bound -= 1
            if upp_bound <= low_bound:
                for i in range(right_bound, left_bound-1, -1):
                    res.append(matrix[low_bound][i])
                low_bound -= 1
            if left_bound <= right_bound:
                for i in range(low_bound, upp_bound-1, -1):
                    res.append(matrix[i][left_bound])
                left_bound += 1
        return res
