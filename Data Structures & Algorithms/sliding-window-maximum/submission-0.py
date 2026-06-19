class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i, _ in enumerate(nums):
            window = nums[i:i + k]
            if len(window) < k:
                break
            output.append(max(window))
        return output
        