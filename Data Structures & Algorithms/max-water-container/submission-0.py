class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for l, l_val in enumerate(heights):
            for r_rev, r_val in enumerate(heights[::-1], 1):
                r = len(heights) - r_rev
                if l >= r:
                    break
                width = r - l
                height = min(l_val, r_val)
                area = width * height
                if area > max_area:
                    max_area = area
        return max_area
        