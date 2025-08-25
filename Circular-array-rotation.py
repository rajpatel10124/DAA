def circularArrayRotation(a, k, queries):
    n = len(a)
    k = k % n   # optimize rotations larger than n
    result = []
    for q in queries:
        # find the original index before rotation
        original_index = (q - k + n) % n
        result.append(a[original_index])
    return result


# Example usage
n, k, q = map(int, input().split())  # number of elements, rotations, queries
a = list(map(int, input().split()))
queries = [int(input()) for _ in range(q)]

ans = circularArrayRotation(a, k, queries)
for val in ans:
    print(val)
