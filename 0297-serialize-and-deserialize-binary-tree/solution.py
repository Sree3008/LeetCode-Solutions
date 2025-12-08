# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        queue = []
        if root:
            queue.append(root)
            res = str(root.val)+" "
        while queue:
            x = []
            for i in queue:
                if i.left:
                    x.append(i.left)
                    res += str(i.left.val)+" "
                else:
                    res += "N "
                if i.right:
                    x.append(i.right)
                    res += str(i.right.val)+" "
                else:
                    res += "N "
            queue = x
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        if data:
            root = TreeNode(int(data.pop(0)))
            queue = [root]
            while data:
                x = []
                for i in queue:
                    if data:
                        if data[0] == "N":
                            data.pop(0)
                        else:
                            i.left = TreeNode(int(data.pop(0)))
                            x.append(i.left)
                    else:
                        break
                    if data:
                        if data[0] == "N":
                            data.pop(0)
                        else:
                            i.right = TreeNode(int(data.pop(0)))
                            x.append(i.right)
                queue = x
            return root
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
