# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, sum):
        
        def dfs(node, target):
            if node:
                if not node.left and not node.right:
                    return (target - node.val) == 0
                return dfs(node.left, target - node.val) or dfs(node.right, target - node.val)
                
        return dfs(root, sum)