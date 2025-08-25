def organizingContainers(container):
    # sum of balls in each container
    container_sums = [sum(row) for row in container]
    
    # sum of balls of each type
    type_sums = [sum(col) for col in zip(*container)]
    
    # check if they can match
    if sorted(container_sums) == sorted(type_sums):
        return "Possible"
    else:
        return "Impossible"


# Example usage
q = int(input())  # number of queries
for _ in range(q):
    n = int(input())
    container = [list(map(int, input().split())) for _ in range(n)]
    print(organizingContainers(container))
