class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        last_val = float("-inf")

        def dfs_in_order(curr):
            nonlocal is_valid, last_val

            if curr is None or not is_valid:
                return
            
            dfs_in_order(curr.left)

            if curr.val <= last_val:
                is_valid = False
                return
            
            last_val = curr.val
            dfs_in_order(curr.right)

        dfs_in_order(root)
        return is_valid