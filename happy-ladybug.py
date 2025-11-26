def happyLadybugs(b):
    counts = {}
    for ch in b:
        counts[ch] = counts.get(ch, 0) + 1

    for k, v in counts.items():
        if k != "_" and v == 1:
            return "NO"

    if "_" in counts:
        return "YES"

    for i in range(len(b)):
        left = i > 0 and b[i] == b[i-1]
        right = i < len(b)-1 and b[i] == b[i+1]
        if not left and not right:
            return "NO"
    return "YES"

g = int(input())
for _ in range(g):
    n = int(input())
    b = input().strip()
    print(happyLadybugs(b))
