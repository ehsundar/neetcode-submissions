# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, None, None)]

        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))
        
        return True
        