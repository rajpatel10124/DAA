def pageCount(n, p):
    # Count pages from front
    from_front = p // 2
    
    # Count pages from back
    from_back = n // 2 - p // 2
    
    # Return the minimum number of turns
    return min(from_front, from_back)

# Main function (HackerRank style)
if __name__ == '__main__':
    n = int(input().strip())  # total pages in book
    p = int(input().strip())  # target page number
    
    result = pageCount(n, p)
    print(result)
