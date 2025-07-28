def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    # Calculate final position of each apple and check if it lands on the house
    for d in apples:
        landing = a + d
        if s <= landing <= t:
            apple_count += 1
    
    # Calculate final position of each orange and check if it lands on the house
    for d in oranges:
        landing = b + d
        if s <= landing <= t:
            orange_count += 1
    
    print(apple_count)
    print(orange_count)


# Input from user
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
