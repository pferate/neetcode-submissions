import itertools

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substr_list = []
        # Break s2 by letters that aren't in s1, adding NULL at end to trigger final append
        running_substr = ""
        for s in s2 + chr(0):
            if s in s1:
                running_substr += s
            else:
                # Ignore any substrs that are shorter than our needle
                if len(running_substr) >= len(s1):
                    substr_list.append(running_substr)
                running_substr = ""

        sorted_s1 = sorted(s1)
        for sub in substr_list:
            for i in range(0, len(sub) - len(s1) + 1):
                substr_chunk = sub[i:i + len(s1)]
                if sorted_s1 == sorted(substr_chunk):
                    return True
        return False
        