class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            try:
                if target < matrix[i + 1][0]:
                    return target in row
            except IndexError:
                return target in row
        