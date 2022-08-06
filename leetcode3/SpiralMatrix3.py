class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> [[int]]:
        res = []
        up_bound = rStart - 1
        low_bound = rStart + 1
        left_bound = cStart - 1
        right_bound = cStart + 1

        row = rStart
        col = cStart


