import math
from functools import reduce

# Helper function to calculate LCM of two numbers
def lcm(x, y):
    return x * y // math.gcd(x, y)

# LCM of list
def lcm_list(arr):
    return reduce(lcm, arr)

# GCD of list
def gcd_list(arr):
    return reduce(math.gcd, arr)

def getTotalX(a, b):
    l = lcm_list(a)
    g = gcd_list(b)
    
    count = 0
    multiple = l
    while multiple <= g:
        if g % multiple == 0:
            count += 1
        multiple += l
        
    return count

# Input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = getTotalX(a, b)
print(result)
