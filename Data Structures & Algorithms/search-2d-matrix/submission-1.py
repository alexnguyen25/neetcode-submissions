class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l <= r:
            m = l + (r - l)//2
            m_rows = m // cols
            m_cols = m % cols

            value = matrix[m_rows][m_cols]
            if value < target:
                l = m + 1
            elif value > target:
                r = m - 1
            elif value == target:
                return True
        return False

        