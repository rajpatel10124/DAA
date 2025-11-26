def countingSort(arr):
    freq = [0] * 100
    for x in arr:
        freq[x] += 1
    result = []
    for i in range(100):
        if freq[i] > 0:
            result.extend([i] * freq[i])
    return result

n = int(input())
arr = list(map(int, input().split()))
print(*countingSort(arr))
