import collections

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        
        graph = collections.defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            graph[u] += v,
            graph[v] += u,
            degree[u] += 1
            degree[v] += 1
        
        q = [node for node in graph if degree[node]==1]
        
        while n>2:
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                n -= 1
                for j in graph[node]:
                    degree[j] -= 1
                    if degree[j]==1:
                        q += j,
       
        return q
        