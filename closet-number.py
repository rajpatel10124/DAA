def closestNumbers(arr):
    arr.sort()
    n = len(arr)

    mindiff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff < mindiff:
            mindiff = diff

    result = []
    for i in range(1, n):
        if arr[i] - arr[i-1] == mindiff:
            result.extend([arr[i-1], arr[i]])

    return result


n = int(input())
arr = list(map(int, input().split()))
print(*closestNumbers(arr))
