def countSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(100)]

    for i in range(n):
        num = int(arr[i][0])
        s = arr[i][1]
        if i < n // 2:
            buckets[num].append("-")
        else:
            buckets[num].append(s)

    result = []
    for b in buckets:
        for s in b:
            result.append(s)

    print(*result)
    
n = int(input())
arr = [input().split() for _ in range(n)]
countSort(arr)
