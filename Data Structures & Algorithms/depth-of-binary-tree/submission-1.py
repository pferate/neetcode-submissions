# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_depth(root, start = 0):
    if root is None:
        return start
    # print(f"root.val: {root.val}, start: {start}")
    left_depth = get_depth(root.left, start + 1)
    right_depth = get_depth(root.right, start + 1)
    return max([left_depth, right_depth])

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return get_depth(root, 0)
        