def flatlandSpaceStations(n, c):
    c.sort()
    max_dist = max(c[0], n - 1 - c[-1])

    for i in range(1, len(c)):
        gap = (c[i] - c[i - 1]) // 2
        if gap > max_dist:
            max_dist = gap
    return max_dist

n, m = map(int, input().split())
c = list(map(int, input().split()))
print(flatlandSpaceStations(n, c))
