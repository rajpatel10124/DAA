def birthday(s, d, m):
    count = 0
    n = len(s)
    
    for i in range(n - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
            
    return count


# Input
n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())

result = birthday(s, d, m)
print(result)
