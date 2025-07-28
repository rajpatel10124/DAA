def migratoryBirds(arr):
    freq = {}
    
    # Count frequency of each bird type
    for bird in arr:
        freq[bird] = freq.get(bird, 0) + 1
    
    # Find maximum frequency
    max_freq = max(freq.values())
    
    # Get all bird ids with max frequency and return the smallest
    result = min([bird_id for bird_id, count in freq.items() if count == max_freq])
    
    return result


# Input
n = int(input())
arr = list(map(int, input().split()))

result = migratoryBirds(arr)
print(result)
