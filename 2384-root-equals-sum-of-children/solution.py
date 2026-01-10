# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        self.res=False
        def recursion(root):
            s=0
            if root.left:
                s+=recursion(root.left)
            if root.right:
                s+=recursion(root.right)
            s+=root.val
            return s
        if root:
            s=recursion(root)-root.val
            if root.val==s:
                return True
        return False
        

