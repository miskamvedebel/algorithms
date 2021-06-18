# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        res = []
        
        def get_tree(root):
            if not root:
                return
            
            res.append(root.val)
            
            if root.left:
                get_tree(root.left)
            if root.right:
                get_tree(root.right)
                
        get_tree(root1)
        get_tree(root2)
        
        return sorted(res)