def acmTeam(topic):
    n = len(topic)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # bitwise OR of two binary strings converted to int
            combined = bin(int(topic[i], 2) | int(topic[j], 2))
            topics_known = combined.count('1')

            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1

    return [max_topics, team_count]


# -------- Main (HackerRank style input) --------
if __name__ == "__main__":
    n, m = map(int, input().split())
    topic = [input().strip() for _ in range(n)]

    result = acmTeam(topic)
    print(result[0])
    print(result[1])
