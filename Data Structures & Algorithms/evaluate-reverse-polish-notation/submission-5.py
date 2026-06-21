from collections import deque


VALID_OPERATORS = "+-*/"

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print(f"tokens: {tokens}")
        stack = deque()
        answer = None
        for token in tokens:
            # print(f"token: {token}")
            if token in VALID_OPERATORS:
                try:
                    r_operand = stack.pop()
                    l_operand = stack.pop()
                except IndexError:
                    print(f"Invalid input: {tokens}. Please try again.")
                    raise
                answer = int(eval(f"{l_operand}{token}{r_operand}"))
                # print(f"answer: {answer}")
                stack.append(answer)
                continue
            try:
                stack.append(int(token))
            except ValueError:
                print(f"Invalid input, tokens must be Integers or {VALID_OPERATORS}, got [{type(token)}]: {token}")
                raise
        if answer is None and len(stack) == 1:
            answer = stack.pop()
        return answer