import heapq

def shortestReach(n, edges, s):
    # Build adjacency list: node -> list of (neighbor, weight)
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Undirected graph

    # Initialize distances with infinity
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[s] = 0

    # Min-heap priority queue: (distance, node)
    heap = [(0, s)]
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        # Skip if we already have a shorter distance
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    # Prepare output, exclude the start node
    result = []
    for node in range(1, n + 1):
        if node == s:
            continue
        result.append(distances[node] if distances[node] != float('inf') else -1)
    
    return result

 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    s = int(input())
    print(*shortestReach(n, edges, s))
