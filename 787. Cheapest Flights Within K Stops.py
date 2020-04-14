import collections
import heapq

def findCheapestPrice(n, flights, src, dst, K):
    edges = collections.defaultdict(dict)
    
    for u, v, w in flights:
        edges[u][v] = w
    
    heap = [(0, src, K+1)]
    
    while heap:
        dist, node, k = heapq.heappop(heap)
        
        if node==dst:
            return dist 
        
        if k>0:
            for neighbor in edges[node]:
                item = (dist + edges[node][neighbor], neighbor, k-1)
                heapq.heappush(heap, item)
    
    return -1