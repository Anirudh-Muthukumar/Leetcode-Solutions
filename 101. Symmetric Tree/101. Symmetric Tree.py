# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        
        q1 = [root]
        q2 = [root]
        ct = 0
        
        while q1:
            size = len(q1)
            
            for _ in range(size):
                node1 = q1.pop(0)
                node2 = q2.pop(0)
                
                if not node1.left and not node2.right :
                    pass
                elif not node1.left or not node2.right:
                    return False
                elif node1.left.val != node2.right.val:
                    return False
                
                if not node1.right and not node2.left :
                    pass
                elif not node1.right or not node2.left:
                    return False
                elif node1.right.val != node2.left.val:
                    return False
                
                if node1.left:
                    q1 += node1.left,
                if node1.right:
                    q1 += node1.right,
                if node2.right:
                    q2 += node2.right,
                if node2.left:
                    q2 += node2.left,
                
                ct+=1
        
        return True
            
        