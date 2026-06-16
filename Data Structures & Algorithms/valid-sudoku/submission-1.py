from collections import Counter
import itertools

class Solution:
    
    def isAllUnique(self, nums: List[str]) -> bool:
        top_2 = Counter(nums).most_common(2)
        for val, count in top_2:
            if val == ".":
                continue
            if count > 1:
                return False
        return True
    
    def isAllUniqueNative(self, nums: List[str]) -> bool:
        filtered_nums = [x for x in nums if x != "."]
        return len(filtered_nums) == len(set(filtered_nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows
        for row in board:
            if not self.isAllUniqueNative(row):
                return False

        # Check Columns
        for y in range(9):
            if not self.isAllUniqueNative([row[y] for row in board]):
                return False

        # Check Squares
        square_map = itertools.product([0,1,2], repeat=2)
        for square in square_map:
            for y_offset in range(0, 9, 3):
                for x_offset in range(0, 9, 3):
                    nums = []
                    for y in range(3):
                        nums += board[y_offset + y][x_offset:x_offset + 3]
                    if not self.isAllUniqueNative(nums):
                        return False
        return True
