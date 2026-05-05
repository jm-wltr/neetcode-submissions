class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Function to transform 1D coordinate to 2D
        def index_bidimensional(pos):
            row = pos // (cols)
            col = pos % cols
            return (row, col)

        # Do binary search over the m*n elements
        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            row, col = index_bidimensional(m)
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr < target:
                l = m + 1
            else:
                r = m - 1

        return False