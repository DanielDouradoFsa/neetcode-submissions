# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #what are the base cases?
        #if an node is null, doenst count
        #if an node exists, count 1?
        #if the right has 3 and left has 2? Should use the max value of this
        if root == None:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

        