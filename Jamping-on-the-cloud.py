def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = 0
    
    while True:
        i = (i + k) % n
        energy -= 1 + 2 * c[i]
        if i == 0:
            break
    return energy


# Taking input from user
n, k = map(int, input().split())
c = list(map(int, input().split()))

print(jumpingOnClouds(c, k))
