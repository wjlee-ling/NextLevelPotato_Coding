"""
인구이동
"""

from collections import deque


def solution():
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def search(y, x):
        q = deque()
        q.append([y, x])
        visited[y][x] = 1

        locs = []
        locs.append([y, x])
        result = board[y][x]
        while q:
            y, x = q.popleft()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < N and 0 <= nx < N and L <= abs(board[y][x] - board[ny][nx]) <= R and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                    locs.append([ny, nx])
                    result += board[ny][nx]

        if len(locs) > 1:
            # print("#", locs)
            for loc in locs:
                y, x = loc
                board[y][x] = result // len(locs)

            # print("@")
            # for b in board:
            #     print(b)
            # print()   

            return True

        return False

    answer = 0
    while True:
        flag = False
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if visited[y][x] == 0:
                    if search(y, x):
                        flag = True
                    # for b in board:
                    #     print(b)
                    # print()

        if flag == False:
            break

        answer += 1

    # for b in board:
    #     print(b)
    # print()
    print(answer)


if __name__ == "__main__":
    solution()
