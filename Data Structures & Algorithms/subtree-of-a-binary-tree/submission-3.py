# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.are_equiv(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def are_equiv(self, r, s) -> bool:
        if r is None:
            return s is None
        
        if s is not None and r.val == s.val:
            return self.are_equiv(r.left, s.left) and self.are_equiv(r.right, s.right)
