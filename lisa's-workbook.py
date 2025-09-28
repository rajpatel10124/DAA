def workbook(n, k, arr):
    special_count = 0
    page = 1  # starting page
    
    for problems in arr:
        for start in range(1, problems + 1, k):  
            end = min(start + k - 1, problems)  # last problem on this page
            # Check if page number is between [start, end]
            if start <= page <= end:
                special_count += 1
            page += 1
    return special_count


# ---------- Main (HackerRank style) ----------
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(workbook(n, k, arr))
