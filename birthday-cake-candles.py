def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = candles.count(tallest)
    return count


# Input from user
n = int(input())
candles = list(map(int, input().split()))

result = birthdayCakeCandles(candles)
print(result)
