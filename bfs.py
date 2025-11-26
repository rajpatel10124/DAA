from collections import deque, defaultdict

def bfs(n, m, edges, s):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize distances (-1 = unreachable)
    dist = [-1] * (n + 1)
    dist[s] = 0

    # BFS
    queue = deque([s])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 6
                queue.append(neighbor)

    # Return distances excluding the start node
    return [dist[i] for i in range(1, n + 1) if i != s]


 
q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    s = int(input())
    result = bfs(n, m, edges, s)
    print(*result)
