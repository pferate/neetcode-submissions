class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = list()
        sorted_nums = sorted(nums)

        positive_sums_indexes = defaultdict(list)
        # Find the indexes of all pairs that are a positive sum (or 0)
        # Assumes list is sorted already
        # y index increases, z index decreases
        # Use the sum as the key for easy look up later
        for y, y_val in enumerate(sorted_nums):
            for z_rev, z_val in enumerate(sorted_nums[::-1], 1):
                z = len(sorted_nums) - z_rev
                if y >= z:
                    break
                total = y_val + z_val
                if total >= 0:
                    positive_sums_indexes[total].append( (y, z) )
        # Find all pairs where the sum is equal to negative x value
        # We can stop once the x value becomes positive (sum of 3 positive values is never 0)
        for x, x_val in enumerate(sorted_nums):
            if x_val > 0:
                break
            for y, z in positive_sums_indexes[-x_val]:
                if len(set([x, y, z])) != 3:
                    continue
                y_val = sorted_nums[y]
                z_val = sorted_nums[z]
                match = sorted([x_val, y_val, z_val])
                if match not in output:
                    output.append(match)
        return output
        