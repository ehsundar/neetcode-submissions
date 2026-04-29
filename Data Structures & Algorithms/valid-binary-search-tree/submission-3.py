# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
    
    def validate(self, root, lower = None, upper = None) -> bool:
        if root is None:
            return True

        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        
        upper_local = min(upper, root.val) if upper is not None else root.val
        lower_local = max(lower, root.val) if lower is not None else root.val

        left_cond = self.validate(root.left, lower, upper_local)
        right_cond = self.validate(root.right, lower_local, upper)

        return left_cond and right_cond
