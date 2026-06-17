class Solution:

    def capture_wather(self, height: List[int], stop_height: int|None = None) -> int:
        capture = False
        last_peak = None
        captured_water = 0
        total_water = 0
        for x, x_val in enumerate(height):
            if last_peak is None:
                last_peak_val = 0
            else:
                last_peak_val = height[last_peak]
            delta_peak = x_val - last_peak_val
            if delta_peak >= 0:
                if capture:
                    total_water += captured_water
                captured_water = 0
                # Ensure the capture bit is set
                capture = True
                last_peak = x
                if stop_height and x_val >= stop_height:
                    break
                continue
            if capture:
                captured_water += -delta_peak
        return total_water
        
    def trap(self, height: List[int]) -> int:
        peak_val = max(height)
        from_left = self.capture_wather(height)
        from_right_until_peak = self.capture_wather(height[::-1], peak_val)
        return from_left + from_right_until_peak
        