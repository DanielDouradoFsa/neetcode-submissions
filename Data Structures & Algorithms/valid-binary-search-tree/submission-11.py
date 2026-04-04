class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        self.last_val = float("-inf")

        def dfs_in_order(curr):
            if curr is None or not self.is_valid:
                return
            
            dfs_in_order(curr.left)

            if curr.val <= self.last_val:
                self.is_valid = False
                return
            
            self.last_val = curr.val
            dfs_in_order(curr.right)

        dfs_in_order(root)
        return self.is_valid