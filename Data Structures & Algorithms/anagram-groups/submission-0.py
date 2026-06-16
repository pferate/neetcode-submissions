from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used_words = []
        output = []
        for i, word in enumerate(strs):
            if word in used_words:
                continue
            current_anagrams = [word]
            used_words.append(word)
            for word2 in strs[i + 1::]:
                if self.isAnagram(word, word2):
                    current_anagrams.append(word2)
                    used_words.append(word2)
            output.append(current_anagrams)
        return output

            
