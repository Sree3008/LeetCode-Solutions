# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        flag=True
        queue=[root]
        res=[]
        while queue:
            x=[]
            y=[]
            for i in queue:
                if i.left:
                    x.append(i.left)
                if i.right:
                    x.append(i.right)
                y.append(i.val)
            if not flag:
                y.reverse()
            res.append(y)
            queue=x
            flag=not flag
        return res
            
            
                
            
        
