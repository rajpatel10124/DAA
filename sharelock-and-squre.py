import math
def sherlock_and_squares(a, b):
    # Calculate the number of perfect squares between a and b (inclusive)
    return math.isqrt(b) - math.isqrt(a - 1)
# Taking input from user
a, b = map(int, input().split())
print(sherlock_and_squares(a, b))

 