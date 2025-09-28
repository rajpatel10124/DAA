def stones(n, a, b):
    last_stones = set()
    for i in range(n):
        last_stone = (n - 1 - i) * a + i * b
        last_stones.add(last_stone)
    return sorted(last_stones)


# -------- Main (HackerRank style) --------
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print(' '.join(map(str, result)))
