# Function to find the index of V in a sorted array
def introTutorial(V, arr):
    # Loop through the array
    for i in range(len(arr)):
        if arr[i] == V:
            return i  # Return the index immediately
    # The problem guarantees that V exists in arr, so we don't need an else


# -------- Main Program --------
if __name__ == "__main__":
    # Read the value to search for
    V = int(input().strip())
    
    # Read the size of the array (not really needed for Python)
    n = int(input().strip())
    
    # Read the array elements as integers
    arr = list(map(int, input().strip().split()))
    
    # Call the function and print the result
    print(introTutorial(V, arr))
