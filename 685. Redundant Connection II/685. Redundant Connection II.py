import collections

class Solution:
    def findRedundantDirectedConnection(self, edges):
        
        parent = collections.defaultdict(list)
        graph = collections.defaultdict(list)
        degree = {}
        n = 0
        
        for u, v in edges:
            graph[u] += v,
            parent[v] += u,
            n = max(n, u, v)
        
        for i in range(1, n+1):
            if len(parent[i]) not in degree:
                degree[len(parent[i])] = 0
            degree[len(parent[i])] += 1
        
        
        for u, v in edges[::-1]:
            # remove current edge u->v
            degree[len(parent[v])] -= 1
            if len(parent[v])-1 not in degree:
                degree[len(parent[v])-1] = 0
            degree[len(parent[v])-1] += 1
            
            if degree[0]==1:
                graph[u].remove(v)
                parent[v].remove(u)
                q = []
                for i in range(1, n+1):
                    if len(parent[i])==0:
                        q += i,
                        break
                visited = set()
   
                while q:
                    node = q.pop(0)
                    visited.add(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            q += nei,
                if len(visited)==n:
                    return [u, v]
                
                parent[v] += u,
                graph[u] += v,
            
            # Backtrack
            degree[len(parent[v])] += 1
            degree[len(parent[v])-1] -= 1
        
        return []
                
            