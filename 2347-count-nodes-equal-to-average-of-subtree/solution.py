# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.c = 0
        def traverse(root):
            su_l = n_l = su_r = n_r = 0
            if root.left:
                su_l,n_l = traverse(root.left)
            if root.right:
                su_r,n_r = traverse(root.right)

            su = root.val + su_l + su_r
            n = n_l + n_r + 1 
            if su//n == root.val:
                self.c+=1
            return su,n
            
        if root:
            traverse(root)
        return self.c
        
