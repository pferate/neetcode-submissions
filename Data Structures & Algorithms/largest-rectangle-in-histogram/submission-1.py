from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        found_rectangle_areas = [0]
        processed_columns = deque([0])
        for x, y1 in enumerate(heights):
            area = y1  # 1 * height
            # Check Right
            for y2 in heights[x + 1:]:
                if y1 <= y2:
                    area += y1
                else:
                    break
            # Check Left
            for y3 in processed_columns:
                if y1 <= y3:
                    area += y1
                else:
                    found_rectangle_areas.append(area)
                    break
            # Move current column to processed
            processed_columns.appendleft(y1)
        return max(found_rectangle_areas)