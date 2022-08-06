class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        res = [[0] * n for _ in range(n)]
        up_bound = 0
        low_bound = n - 1
        left_bound = 0
        right_bound = n - 1
        i = 1
        while i <= (n * n):
            if up_bound <= low_bound:
                for j in range(left_bound, right_bound+1):
                    res[up_bound][j] = i
                    i += 1
                up_bound += 1

            if left_bound <= right_bound:
                for j in range(up_bound, low_bound+1):
                    res[j][right_bound] = i
                    i += 1
                right_bound -= 1

            if up_bound <= low_bound:
                for j in range(right_bound, left_bound-1, -1):
                    res[low_bound][j] = i
                    i += 1
                low_bound -= 1

            if left_bound <= right_bound:
                for j in range(low_bound, up_bound-1, -1):
                    res[j][left_bound] = i
                    i += 1
                left_bound += 1
        return res
