from collections import deque

def quickestWayUp(ladders, snakes):
    # Build the board mapping
    board = {i: i for i in range(1, 101)}
    for start, end in ladders + snakes:
        board[start] = end

    # BFS initialization
    visited = [False] * 101
    queue = deque([(1, 0)])  # (square, moves)
    visited[1] = True

    while queue:
        current, moves = queue.popleft()

        if current == 100:
            return moves

        # Try all die rolls
        for roll in range(1, 7):
            next_square = current + roll
            if next_square <= 100 and not visited[board[next_square]]:
                visited[board[next_square]] = True
                queue.append((board[next_square], moves + 1))

    return -1

 
t = int(input())
for _ in range(t):
    ladders = []
    snakes = []
    n_ladders = int(input())
    for _ in range(n_ladders):
        start, end = map(int, input().split())
        ladders.append((start, end))

    n_snakes = int(input())
    for _ in range(n_snakes):
        start, end = map(int, input().split())
        snakes.append((start, end))

    print(quickestWayUp(ladders, snakes))
