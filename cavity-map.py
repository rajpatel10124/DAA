def cavityMap(grid):
    n = len(grid)
    # Convert rows to lists for mutability
    grid = [list(row) for row in grid]
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            cell = grid[i][j]
            # Check adjacent cells
            if (cell > grid[i-1][j] and
                cell > grid[i+1][j] and
                cell > grid[i][j-1] and
                cell > grid[i][j+1]):
                grid[i][j] = 'X'
    
    # Convert rows back to strings
    return [''.join(row) for row in grid]


# -------- Main (HackerRank style) --------
if __name__ == "__main__":
    n = int(input().strip())
    grid = [input().strip() for _ in range(n)]
    result = cavityMap(grid)
    for row in result:
        print(row)
