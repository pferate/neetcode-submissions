import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i, val in enumerate(nums):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            output.append(math.prod(nums_copy))
        return output
        