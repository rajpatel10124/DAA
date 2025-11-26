# Fenwick Tree (Binary Indexed Tree)
class Fenwick:
    def __init__(self, n):
        self.fw = [0] * (n + 1)

    def update(self, i, v):
        while i < len(self.fw):
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s


def insertionSort(arr):
    # coordinate compression
    vals = sorted(set(arr))
    comp = {v: i+1 for i, v in enumerate(vals)}

    fenwick = Fenwick(len(vals))
    shifts = 0

    for x in arr:
        idx = comp[x]
        greater = fenwick.query(len(vals)) - fenwick.query(idx)
        shifts += greater
        fenwick.update(idx, 1)

    return shifts


# reading input
q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(insertionSort(arr))
