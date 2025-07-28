def bonAppetit(bill, k, b):
    # Calculate total bill excluding item k
    total_excluding_k = sum(bill) - bill[k]
    
    # Calculate Anna's share
    anna_share = total_excluding_k // 2
    
    # Check if charged amount equals her share
    if b == anna_share:
        print("Bon Appetit")
    else:
        # Print overcharged amount
        print(b - anna_share)


# Input
n, k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())

# Function call
bonAppetit(bill, k, b)
