class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i, i_val in enumerate(temperatures):
            higher_found = False
            for j, j_val in enumerate(temperatures[i + 1:], 1):
                if i_val < j_val:
                    output.append(j)
                    higher_found = True
                    break
            if not higher_found:
                output.append(0)
        return output