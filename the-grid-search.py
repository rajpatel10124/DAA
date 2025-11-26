def gridSearch(G, P):
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            if G[i][j:j+c] == P[0]:
                match = True
                for k in range(1, r):
                    if G[i+k][j:j+c] != P[k]:
                        match = False
                        break
                if match:
                    return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    R, C = map(int, input().split())
    G = [input() for _ in range(R)]
    r, c = map(int, input().split())
    P = [input() for _ in range(r)]
    print(gridSearch(G, P))
