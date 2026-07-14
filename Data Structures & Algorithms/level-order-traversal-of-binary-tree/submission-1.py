# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        out = []
        while queue:
            temp = []
            for node in queue:
                temp.append(node.val)
            out.append(temp)
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
        return out
            
