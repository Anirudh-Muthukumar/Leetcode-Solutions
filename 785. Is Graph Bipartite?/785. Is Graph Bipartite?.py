import collections

class Solution:
    def isBipartite(self, Graph):
        graph = collections.defaultdict(list)
        
        for i in range(len(Graph)):
            for edge in Graph[i]:
                graph[i] += edge,
        
        
        node_color = {}
        visited = set()
        
        for i in graph:
            if i not in visited:
                q = [(i, 1)]
                
                while q:
                    node, color = q.pop()
                    visited.add(node)
                    node_color[node] = color
                    
                    for nei in graph[node]:
                        if nei not in visited: # if not colored, color the node
                            q += (nei, 1-color),
                        elif node_color[nei]!=(1-color): # if colored, check if color matches
                            return False
                    
        return True
            