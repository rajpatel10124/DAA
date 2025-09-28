def nonDivisibleSubset(k, S):
    # Count remainders
    count = [0] * k
    for num in S:
        count[num % k] += 1

 
    result = min(count[0], 1)

    # Check each remainder pair
    for i in range(1, (k // 2) + 1):
        if i == k - i:   
            result += 1
        else:
            result += max(count[i], count[k - i])

    return result


 
n, k = map(int, input().split())
S = list(map(int, input().split()))

print(nonDivisibleSubset(k, S))
