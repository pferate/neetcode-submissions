from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        most_common = Counter(nums).most_common(1)
        if len(most_common) > 0:
            most_common_value, most_common_count = most_common[0]
            return most_common_count > 1
        else:
            return False