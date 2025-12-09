# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split()))
        self.i = 0

        def build(lower, upper):
            if self.i == len(vals):
                return None
            val = vals[self.i]
            if val < lower or val > upper:
                return None

            self.i += 1
            root = TreeNode(val)
            root.left = build(lower, val)
            root.right = build(val, upper)
            return root

        return build(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
