def find_digits(n):
    count = 0
    for digit in str(n):
        d = int(digit)
        if d != 0 and n % d == 0:
            count += 1
    return count

t = int(input())   
for _ in range(t):
    n = int(input())
    print(find_digits(n))



