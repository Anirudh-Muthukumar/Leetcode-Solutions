# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # BST gives ascending order of numbers in inorder traversal
        
        stack = []
        res = []
        
        while stack or root:
            
            while root:
                stack += root,
                root = root.left
            
            root = stack.pop()
            if res and root.val <= res[-1]:
                return False
            res += root.val,
            root = root.right
        
        return True