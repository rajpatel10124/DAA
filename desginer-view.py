def designerPdfViewer(h, word):
    # Find the maximum height among the letters in the word
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')
        max_height = max(max_height, h[index])
    
    # Area = max_height * length of the word (width per char is 1)
    return max_height * len(word)

# Input reading from stdin (as per HackerRank)
if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
