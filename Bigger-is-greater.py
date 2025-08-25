def biggerIsGreater(w):
    w = list(w)  # convert string to list for mutability
    n = len(w)

    # Step 1: find first character from end which is smaller than next
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    # Step 2: find the smallest character greater than w[i] to the right
    j = n - 1
    while w[j] <= w[i]:
        j -= 1

    # Step 3: swap
    w[i], w[j] = w[j], w[i]

    # Step 4: reverse the substring after i
    w[i + 1:] = reversed(w[i + 1:])

    return "".join(w)


# HackerRank style input/output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w = input().strip()
        print(biggerIsGreater(w))
