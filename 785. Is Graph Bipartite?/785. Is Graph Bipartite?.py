import collections

class Solution:
    def isBipartite(self, graph):
        visited = collections.defaultdict()
        for i in range(len(graph)):
            if i not in visited:
                q = collections.deque([(i, 0)])
                visited[i] = 0
                while q:
                    node, color = q.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            q.append((nei, 1-color))
                            visited[nei] = 1-color
                        elif nei in visited and visited[nei]!=(1-color):
                            return False
                
        return True
                
        