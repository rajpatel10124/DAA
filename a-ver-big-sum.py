def sum_array(arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
        
    return sum

n=int(input())
arr=list(map(int,input().split()))


    
print(sum_array(arr))
