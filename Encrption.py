import math

def encryption(s):
    # Remove spaces
    s = s.replace(" ", "")
    L = len(s)

    # Compute rows and columns
    rows = int(math.floor(math.sqrt(L)))
    cols = int(math.ceil(math.sqrt(L)))
    if rows * cols < L:
        rows += 1

    # Create encrypted message
    encrypted_words = []
    for c in range(cols):
        word = ""
        for r in range(c, L, cols):
            word += s[r]
        encrypted_words.append(word)

    return " ".join(encrypted_words)


# HackerRank style input/output
if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
