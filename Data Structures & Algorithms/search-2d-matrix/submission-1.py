class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            row, col = m // cols, m % cols
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr < target:
                l = m + 1
            else:
                r = m - 1

        return False