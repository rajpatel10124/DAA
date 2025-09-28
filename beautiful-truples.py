def beautifulTriplets(d, arr):
    s = set(arr)
    count = 0
    for x in arr:
        if (x + d in s) and (x + 2*d in s):
            count += 1
    return count


# -------- Main (HackerRank style input) --------
if __name__ == "__main__":
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(beautifulTriplets(d, arr))
