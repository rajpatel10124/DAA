def equalizeArray(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

    return len(arr) - max_freq


 
n = int(input())   
arr = list(map(int, input().split()))   
print(equalizeArray(arr))
