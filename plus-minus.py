def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    
    # Print ratios with 6 decimal places
    print("{0:.6f}".format(pos / n))
    print("{0:.6f}".format(neg / n))
    print("{0:.6f}".format(zero / n))


# Input from user
n = int(input())
arr = list(map(int, input().split()))

plusMinus(arr)
