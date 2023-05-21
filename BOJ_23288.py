from collections import deque


def solution():
    answer = 0
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 동남서북
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    dice1 = deque([1, 3, 6, 4])  # 동, 서 방향
    dice2 = deque([1, 2, 6, 5])  # 북, 남 방향

    def dice_move(dir):
        if dir == 0:  # 동(우)
            dice1.rotate()
            dice2[0], dice2[2] = dice1[0], dice1[2]
        elif dir == 1:  # 남(하)
            dice2.rotate(-1)
            dice1[0], dice1[2] = dice2[0], dice2[2]
        elif dir == 2:  # 서(좌)
            dice1.rotate(-1)
            dice2[0], dice2[2] = dice1[0], dice1[2]
        elif dir == 3:  # 북(상)
            dice2.rotate()
            dice1[0], dice1[2] = dice2[0], dice2[2]

    def bfs(row, col, score):
        result = score
        q = deque()
        q.append([row, col])
        visited = [[0] * M for _ in range(N)]
        visited[row][col] = 1

        while q:
            y, x = q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and board[ny][nx] == score:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
                    result += score

        return result

    direction = 0

    y, x = 0, 0
    for i in range(K):
        ny = y + dy[direction]
        nx = x + dx[direction]

        if not (0 <= ny < N and 0 <= nx < M):  # 반대 방향
            direction = (direction + 2) % 4
            ny = y + dy[direction]
            nx = x + dx[direction]

        y = ny
        x = nx
        dice_move(direction)
        under_num = dice1[2]  # A
        score = board[y][x]  # B
        answer += bfs(y, x, score)

        if under_num > score:  # 90도 시계 방향 회전
            direction = (direction + 1) % 4

        elif under_num < score:  # 90도 반시계 방향 회전
            direction = (direction - 1) % 4

    print(answer)


if __name__ == "__main__":
    solution()
