# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True

        def dfs_in_order(curr, last_val):
            if curr is None:
                return last_val

            last_val = dfs_in_order(curr.left, last_val)

            if curr.val <= last_val:
                self.is_valid = False
                return last_val

            last_val = curr.val

            return dfs_in_order(curr.right, last_val)

        dfs_in_order(root, float("-inf"))
        return self.is_valid