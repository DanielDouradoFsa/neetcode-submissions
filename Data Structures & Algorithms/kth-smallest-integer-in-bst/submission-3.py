# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        current_smallest = root.val
        def dfs_in_order(curr):
            nonlocal cnt, current_smallest
            if curr is None:
                return
            dfs_in_order(curr.left)
            cnt-=1
            if cnt==0:
                current_smallest = curr.val
                return
            dfs_in_order(curr.right)

        dfs_in_order(root)
        return current_smallest