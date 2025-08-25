def permutationEquation(p):
    # build position map (value -> index+1)
    pos = {}
    for idx, val in enumerate(p, start=1):
        pos[val] = idx
    
    result = []
    for x in range(1, len(p) + 1):
        # find y such that p(p(y)) = x
        y = pos[pos[x]]
        result.append(y)
    return result


# Example usage
n = int(input())
p = list(map(int, input().split()))

ans = permutationEquation(p)
for val in ans:
    print(val)
