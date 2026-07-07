# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
        #     print(f"PRE: root.val: {root.val}")
        #     if root.left:
        #         print(f"PRE: root.left.val: {root.left.val}")
        #     else:
        #         print(f"PRE: root.left: {root.left}")
        #     if root.right:
        #         print(f"PRE: root.right.val: {root.right.val}")
        #     else:
        #         print(f"PRE: root.right: {root.right}")
            new_right = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(new_right)
        #     print(f"POST: root.val: {root.val}")
        #     if root.left:
        #         print(f"POST: root.left.val: {root.left.val}")
        #     else:
        #         print(f"POST: root.left: {root.left}")
        #     if root.right:
        #         print(f"POST: root.right.val: {root.right.val}")
        #     else:
        #         print(f"POST: root.right: {root.right}")
        # else:
        #     print(f"root: {root}")
        return root