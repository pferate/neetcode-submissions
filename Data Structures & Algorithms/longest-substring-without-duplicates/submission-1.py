from collections import Counter

def all_unique(s: str) -> bool:
    if len(s) == 0:
        return 0
    cntr = Counter(s)
    _, max = cntr.most_common()[0]
    return max == 1

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        best_index = 0
        most_unique = 1
        increase_index = False
        end_found = False
        for i, _ in enumerate(s):
            # print(f"i: {i}, best_index: {best_index}, most_unique: {most_unique}")
            counter = 0
            while True:
                counter += 1
                if counter > len(s) + 2:
                    # print("Loop found!")
                    break
                current_unique = most_unique + 1
                end = i + current_unique
                substr = s[i:end]
                # print(f"substr: {substr}")
                if len(s) < end:
                    # print("We've reached the end!")
                    end_found = True
                    break
                if all_unique(substr):
                    best_index = i
                    most_unique += 1
                    continue
                # print("Duplicate found :(")
                break
            if end_found:
                break
        return most_unique
        