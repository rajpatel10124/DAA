def pickingNumbers(a):
    freq = [0] * 101  # Since elements are <= 100 as per constraints

    # Count the frequency of each number
    for number in a:
        freq[number] += 1

    max_length = 0

    # Check the maximum sum of frequency[i] + frequency[i+1]
    for i in range(100):
        max_length = max(max_length, freq[i] + freq[i+1])

    return max_length

# HackerRank-style input handling
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
