class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxdep = [0]

        def traverse(node, l=1):
            if node is None:
                return
            maxdep[0] = max(maxdep[0], l)

            if node.children:
                for child in node.children:
                    traverse(child, l+1)

        traverse(root)
        return maxdep[0]

