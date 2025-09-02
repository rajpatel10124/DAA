def extra_long_factorials(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * extra_long_factorials(n - 1)

# Taking input from user
n = int(input())
print(extra_long_factorials(n))
