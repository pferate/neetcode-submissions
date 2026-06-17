from collections import Counter

def good_after_replacement(s: str, k: int) -> bool:
    if len(s) == 0:
        return 0
    cntr = Counter(s)
    # If we have only one most common character, it's all unique
    if len(cntr.most_common()) == 1:
        return True
    # The sum of all other characters must be equal to or less than the number we are replacing
    remaining_count = cntr.total() - cntr.most_common()[0][1]
    return remaining_count <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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
                if good_after_replacement(substr, k):
                    best_index = i
                    most_unique += 1
                    continue
                # print("Duplicate found :(")
                break
            if end_found:
                break
        return most_unique
