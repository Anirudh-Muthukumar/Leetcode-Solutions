import collections

class Solution:
    def networkDelayTime(self, times, N, K):
        
        graph = collections.defaultdict(collections.defaultdict)
        for u, v, w in times:
            graph[u][v] = w
        
        q = [(K, 0)]
        res = 0
        visited = set()
        time_taken = {}
        while q:
            temp = set()
            for node, time in q:
                visited.add(node)
                if node in time_taken:
                    time_taken[node] = min(time_taken[node], time)
                else:
                    time_taken[node] = time

                for nei in graph[node]:
                    if nei not in visited: 
                        temp.add((nei, time + graph[node][nei]))
                    elif nei in visited and time_taken[nei] > time + graph[node][nei]:
                        temp.add((nei, time + graph[node][nei]))
            q = temp

        if len(visited)<N:
            return -1
        
        for node in time_taken:
            res = max(res, time_taken[node])
        
        return res