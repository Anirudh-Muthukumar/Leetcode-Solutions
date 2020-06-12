import collections

class Solution:
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(list)
        count = {}
        for u, v in edges:
            graph[u] += v,
            graph[v] += u,
        
        n = len(graph)
        
        for i in range(len(edges)-1, -1, -1):
            u, v = edges[i]
            graph[u].remove(v)
            graph[v].remove(u)
            q = [1]
            visited = set()
            while q:
                node = q.pop()
                visited.add(node)
                
                for nei in graph[node]:
                    if nei not in visited:
                        q += nei,
            
            if len(visited)==n:
                return edges[i]
            
            graph[u] += v,
            graph[v] += u,
        
        return []