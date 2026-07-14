# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        res = []
        def preorder(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        values = data.split(",")
        i = 0
    
        def dfs():
            nonlocal i
            if values[i] == "N":
                i+=1
                return None
            node = TreeNode(int(values[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


