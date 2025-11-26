def strangeCounter(t):
    cycle = 3
    while t > cycle:
        t -= cycle
        cycle *= 2
    return cycle - t + 1

t = int(input())
print(strangeCounter(t))
