class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x, x_val in enumerate(numbers, 1):
            for y, y_val in enumerate(numbers[x - 1::], x):
                if x_val + y_val == target:
                    return [x, y]
                if x_val + y_val > target:
                    break
        