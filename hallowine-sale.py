def howManyGames(p, d, m, s):
    games = 0
    cost = p
    
    while s >= cost:
        s -= cost
        games += 1
        cost = max(cost - d, m)  
    
    return games


p, d, m, s = map(int, input().split())
print(howManyGames(p, d, m, s))
