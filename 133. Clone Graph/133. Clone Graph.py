import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node'):
        if not node:
            return 
        
        dic = collections.defaultdict(Node)
        nodeCopy = Node(node.val)
        dic[node] = nodeCopy
        q = [node]
        
        while q:
            node = q.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors += neighborCopy,
                    q += neighbor,
                else:
                    dic[node].neighbors += dic[neighbor],
        
        return nodeCopy