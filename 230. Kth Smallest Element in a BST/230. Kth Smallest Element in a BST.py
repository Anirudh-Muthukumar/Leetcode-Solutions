# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        
        res = []
        
        def InOrder(node):
            if node:
                InOrder(node.left)
                res.append(node.val)
                InOrder(node.right)
        
        InOrder(root)
        
        return res[k-1]
            