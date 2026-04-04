# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #an root can be viewed from the right side if doesnt have 
        #if i do an BFS, the first position will be the answear
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            n_levels = len(queue)
            has_inserted = False
            for _ in range(n_levels):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if not has_inserted:
                    result.append(node.val)
                    has_inserted = True
        return result
"""
"""
        