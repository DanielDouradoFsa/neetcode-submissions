# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_good_nodes = 0
        def dfs_pre_order(root, max_until_now):
            if not root:
                return
            if root.val >= max_until_now:
                self.num_good_nodes += 1
                max_until_now = root.val
            dfs_pre_order(root.left, max_until_now)
            dfs_pre_order(root.right, max_until_now)
        dfs_pre_order(root, float("-inf"))
        return self.num_good_nodes
        