def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0
    
    for s in scores[1:]:
        if s > max_score:
            max_score = s
            max_count += 1
        elif s < min_score:
            min_score = s
            min_count += 1
            
    return [max_count, min_count]


# Input
n = int(input())
scores = list(map(int, input().split()))

result = breakingRecords(scores)
print(result[0], result[1])
