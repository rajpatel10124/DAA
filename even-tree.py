from collections import defaultdict

def evenForest(t_nodes, t_edges, t_from, t_to):
    # Build adjacency list
    tree = defaultdict(list)
    for u, v in zip(t_from, t_to):
        tree[u].append(v)
        tree[v].append(u)

    visited = [False] * (t_nodes + 1)
    removable_edges = 0

    def dfs(node):
        nonlocal removable_edges
        visited[node] = True
        size = 1  # count itself
        for neighbor in tree[node]:
            if not visited[neighbor]:
                subtree_size = dfs(neighbor)
                if subtree_size % 2 == 0:
                    removable_edges += 1  # cut this edge
                else:
                    size += subtree_size  # add to current subtree
        return size

    dfs(1)  # root at node 1
    return removable_edges
 
 
t_nodes, t_edges = map(int, input().split())
t_from, t_to = [], []

for _ in range(t_edges):
    u, v = map(int, input().split())
    t_from.append(u)
    t_to.append(v)

print(evenForest(t_nodes, t_edges, t_from, t_to))
