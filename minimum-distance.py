def minimumDistances(a):
    last_seen = {}
    min_dist = float('inf')

    for i, value in enumerate(a):
        if value in last_seen:
            dist = i - last_seen[value]
            min_dist = min(min_dist, dist)
        last_seen[value] = i

    return min_dist if min_dist != float('inf') else -1


n = int(input())
arr = list(map(int, input().split()))
print(minimumDistances(arr))
