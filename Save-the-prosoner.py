def saveThePrisoner(n, m, s):
    last = (s + m - 1) % n
    return last if last != 0 else n


# Example usage with multiple test cases:
t = int(input())  # number of test cases
for _ in range(t):
    n, m, s = map(int, input().split())
    print(saveThePrisoner(n, m, s))
