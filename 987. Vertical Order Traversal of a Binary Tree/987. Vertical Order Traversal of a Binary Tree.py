import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root):
        
        def dfs(node, x=0, y=0):
            if node:
                seen[x][y] += node,
                if node.left:
                    dfs(node.left, x-1, y+1)
                if node.right:
                    dfs(node.right, x+1, y+1)
        
        seen = collections.defaultdict(lambda:collections.defaultdict(list))
        dfs(root)
        res = []
        for x in sorted(seen):
            temp = []
            for y in sorted(seen[x]):
                temp.extend(sorted(node.val for node in seen[x][y]))
            res += temp,
        return res
        
            