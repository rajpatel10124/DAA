def fairRations(B):
    # If sum is odd, it's impossible
    if sum(B) % 2 != 0:
        return "NO"
    
    count = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:      # If odd
            B[i] += 1
            B[i+1] += 1
            count += 2
    return str(count)


# -------- Main (HackerRank style) --------
if __name__ == "__main__":
    n = int(input().strip())
    B = list(map(int, input().split()))
    print(fairRations(B))
