def hurdleRace(k, height):
    max_hurdle = max(height)
    return max(0, max_hurdle - k)

# Input/output handling (for HackerRank)
if __name__ == '__main__':
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    print(result)
