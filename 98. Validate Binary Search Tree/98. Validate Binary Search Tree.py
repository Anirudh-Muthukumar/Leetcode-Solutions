# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        # inorder traversal should give ascending order
        inorder = []
        stack = []
        
        while root or stack:
            while root!=None:
                stack += root,
                root = root.left
            
            root = stack.pop()
            
            if len(inorder)>=1 and inorder[-1] >= root.val:
                return False
            
            inorder += root.val,
            root = root.right
        
        return True
            
            
                
            