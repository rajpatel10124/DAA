def cutTheSticks(arr):
    result = []
    arr.sort()  
    
    while arr:   
        result.append(len(arr))   
        cut = arr[0]   
 
        arr = [x - cut for x in arr if x - cut > 0]
    
    return result


n = int(input())   
arr = list(map(int, input().split()))   
answer = cutTheSticks(arr)

for num in answer:
    print(num)
