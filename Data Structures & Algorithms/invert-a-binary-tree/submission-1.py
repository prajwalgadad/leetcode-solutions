# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return
            # post order
            l = helper(root.left)
            r = helper(root.right)
            # what is coming from down = r, l
            # r and l is connected to root, now we want to invert the connection
            root.left = r
            root.right = l
            return root
        return helper(root)