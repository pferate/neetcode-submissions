class Solution:

    def isValid(self, s: str) -> bool:
        # We can use either a list or deque
        opened = []
        for i in s:
            if i in ["(", "{", "["]:
                opened.append(i)
                continue
            # We should only be seeing closing items at this point
            if not opened:
                return False
            # We can totally optimize this into a single check, but using simple for now
            if i == ")" and opened[-1] != "(":
                return False
            if i == "}" and opened[-1] != "{":
                return False
            if i == "]" and opened[-1] != "[":
                return False
            # Doubly ensure that we have an expected closing before popping from the list/queue
            if i in [")", "}", "]"]:
                opened.pop()
                continue
            raise ValueError(f"Found unexpected character: {i}")
        if opened:
            return False
        return True
