class Solution:

    DELIMITER = chr(0)

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return self.DELIMITER + self.DELIMITER.join(strs)

    def decode(self, s: str) -> List[str]:
        if s:
            return s[1::].split(self.DELIMITER)
        return []
