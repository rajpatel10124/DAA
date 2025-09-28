def serviceLane(n, cases, width):
    results = []
    for i, j in cases:
        results.append(min(width[i:j+1]))   
    return results


# -------- Main (HackerRank style) --------
if __name__ == "__main__":
    n, t = map(int, input().split())
    width = list(map(int, input().split()))
    cases = [tuple(map(int, input().split())) for _ in range(t)]
    
    results = serviceLane(n, cases, width)
    for res in results:
        print(res)
