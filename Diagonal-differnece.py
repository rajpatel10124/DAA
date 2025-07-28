def diagonalDifference(arr):
    n = len(arr)
    primary = 0
    secondary = 0
    
    for i in range(n):
        primary += arr[i][i]           # primary diagonal
        secondary += arr[i][n-1-i]     # secondary diagonal
        
    return abs(primary - secondary)


# Input from user
n = int(input())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

result = diagonalDifference(arr)
print(result)

