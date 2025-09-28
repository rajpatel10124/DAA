def chocolateFeast(n, c, m):
    chocolates = n // c          # initial chocolates Bobby can buy
    wrappers = chocolates
    
    while wrappers >= m:
        free = wrappers // m     # trade wrappers for free chocolates
        chocolates += free
        wrappers = wrappers % m + free  # remaining + new wrappers
    
    return chocolates


# -------- Main (HackerRank style) --------
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n, c, m = map(int, input().split())
        print(chocolateFeast(n, c, m))
