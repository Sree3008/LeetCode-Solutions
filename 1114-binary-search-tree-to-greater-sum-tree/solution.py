# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root,x=0):
            if root.right:
                x=traverse(root.right,x) 
            root.val+=x
            x=root.val
            if root.left:
                x=traverse(root.left,x)
            return x
        if root:
            traverse(root)
        return root
        
