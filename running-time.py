def runningTime(arr):
    shifts = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
         
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift occurs
            shifts += 1
            j -= 1
        
        arr[j + 1] = key   
    
    return shifts


 
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(runningTime(arr))
