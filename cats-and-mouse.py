def catAndMouse(x, y, z):
    dist_catA = abs(x - z)
    dist_catB = abs(y - z)

    if dist_catA < dist_catB:
        return "Cat A"
    elif dist_catB < dist_catA:
        return "Cat B"
    else:
        return "Mouse C"

# Reading input
q = int(input())  # number of queries

for _ in range(q):
    x, y, z = map(int, input().split())
    result = catAndMouse(x, y, z)
    print(result)
