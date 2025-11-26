import math

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    if end < start:
        return 0
    return end - start + 1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(squares(a, b))
