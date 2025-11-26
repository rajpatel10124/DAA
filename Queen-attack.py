def queensAttack(n, k, r_q, c_q, obstacles):
    obs = {(r, c) for r, c in obstacles}
    
    count = 0
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    for dr, dc in directions:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obs:
            count += 1
            r += dr
            c += dc
    return count

n, k = map(int, input().split())
r_q, c_q = map(int, input().split())
obstacles = [tuple(map(int, input().split())) for _ in range(k)]

print(queensAttack(n, k, r_q, c_q, obstacles))
