# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        q = [(root, 1)]
        
        res = []
        
        while q:
            node, depth = q.pop(0)
            
            if len(res) < depth : # first node of each level
                res += node.val,
            
            if node.right:
                q += (node.right, depth+1), # visit right child first
            if node.left:
                q += (node.left, depth+1),
            
        return res