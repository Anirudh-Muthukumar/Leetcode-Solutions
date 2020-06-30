import collections

class Solution:
    def eventualSafeNodes(self, graph):
        # WHITE - GRAY - BLACK DFS
        
        # mark a node GRAY on entry, BLACK on exit
        WHITE, GRAY, BLACK = 0, 1, 2
        
        color = collections.defaultdict(int)
        
        def dfs(node):
            if color[node]!=WHITE:
                return color[node]==BLACK
            
            color[node] = GRAY
            
            for nei in graph[node]:
                if color[nei]==BLACK: # leading to a terminal node
                    continue
                if color[nei]==GRAY or not dfs(nei): # leading to a cycle
                    return False
            
            color[node] = BLACK
            return True
        
        return filter(dfs, range(len(graph)))