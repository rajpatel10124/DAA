def insertionSort1(n, arr):
    key = arr[-1]  # Last element
    i = n - 2      # Start comparing from the second last element
    
    
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]  # Shift
        print(' '.join(map(str, arr)))
        i -= 1
    
     
    arr[i+1] = key
    print(' '.join(map(str, arr)))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    insertionSort1(n, arr)
