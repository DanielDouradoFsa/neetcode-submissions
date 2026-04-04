# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.results = []
        self.is_valid = True
        def bfs_in_order(curr):
            if curr is None:
                return
            bfs_in_order(curr.left)

            if len(self.results) > 0 and curr.val <= self.results[-1]:
                self.is_valid = False
                print("wrong value: ", curr.val)
            self.results.append(curr.val)
            bfs_in_order(curr.right)
        bfs_in_order(root)
        print(self.results)
        return self.is_valid
        