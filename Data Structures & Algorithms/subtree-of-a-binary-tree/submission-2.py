# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serializeTree(root):
            if root is None:
                return "-"
            leftPart = serializeTree(root.left)
            rightPart = serializeTree(root.right)
            return f"{root.val}{leftPart}{rightPart}"
        bigger_tree_str = serializeTree(root)
        sub_tree_str = serializeTree(subRoot)
        return sub_tree_str in bigger_tree_str