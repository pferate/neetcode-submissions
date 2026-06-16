class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        running_longest = 0
        last = None
        for i in sorted(set(nums)):
            if last is None or i - last == 1:
                running_longest += 1
            else:
                if running_longest > longest:
                    longest = running_longest
                running_longest = 1
            last = i
            if running_longest > longest:
                longest = running_longest
        return longest
        