def countingSort(arr):
    freq = [0] * 100
    for x in arr:
        freq[x] += 1
    return freq

n = int(input())
arr = list(map(int, input().split()))
print(*countingSort(arr))
