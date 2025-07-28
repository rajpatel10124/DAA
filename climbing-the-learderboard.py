def climbingLeaderboard(ranked, player):
    # Step 1: Remove duplicates and sort descending
    unique_ranked = sorted(set(ranked), reverse=True)
    n = len(unique_ranked)
    result = []
    
    # Step 2: Initialize pointer for ranked list from the end
    i = n - 1

    # Step 3: Iterate through each player's score
    for score in player:
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1
        # i is the index of the last score greater than current score
        result.append(i + 2)  # rank is index + 2

    return result


# HackerRank-compatible I/O format
if __name__ == '__main__':
    n = int(input())
    ranked = list(map(int, input().rstrip().split()))
    m = int(input())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    for r in result:
        print(r)
