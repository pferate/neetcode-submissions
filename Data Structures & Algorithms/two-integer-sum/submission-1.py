class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value_i in enumerate(nums):
            for rel_j, value_j in enumerate(nums[i + 1::]):
                if value_i + value_j == target:
                    return [i, i + rel_j + 1]