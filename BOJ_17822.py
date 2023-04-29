from collections import deque


def solution():
    N, M, T = map(int, input().split())
    board = [deque(list(map(int, input().split()))) for _ in range(N)]

    # for b in board:
    #     print(b)
    # print()

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(i, j):
        visited = [[0] * M for _ in range(N)]
        result = 0

        q = deque()
        q.append([i, j])
        visited[i][j] = 1

        while q:
            y, x = q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = (x + dx[d]) % M

                if 0 <= ny < N and 0 <= nx < M and board[i][j] == board[ny][nx] and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                    result += 1

        if result:
            for y in range(N):
                for x in range(M):
                    if visited[y][x] == 1:
                        board[y][x] = 0

        return result

    for _ in range(T):
        x, d, k = map(int, input().split())

        for i in range(1, N + 1):
            if i % x != 0:
                continue

            i -= 1
            if d == 0:
                for _ in range(k):
                    board[i].rotate()

            else:
                for _ in range(k):
                    board[i].rotate(-1)

        # for b in board:
        #     print(b)
        # print()

        flag = True
        for row in range(N):
            for col in range(M):
                if board[row][col] == 0:
                    continue
                change = bfs(row, col)
                if change:
                    flag = False

        if flag:
            cnt = 0
            total = 0
            for row in range(N):
                for col in range(M):
                    if board[row][col]:
                        cnt += 1
                        total += board[row][col]

            for row in range(N):
                for col in range(M):
                    if board[row][col] > 0:
                        if board[row][col] > total / cnt:
                            board[row][col] -= 1
                        elif board[row][col] < total / cnt:
                            board[row][col] += 1

        # for b in board:
        #     print(b)
        # print()

    answer = 0
    for b in board:
        answer += sum(b)
    return answer


if __name__ == "__main__":
    print(solution())
