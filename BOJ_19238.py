from collections import deque


def solution():
    N, M, F = map(int, input().split())
    global answer
    answer = F
    board = [list(map(int, input().split())) for _ in range(N)]
    temp_board = [[0] * N for _ in range(N)]

    taxi_y, taxi_x = map(int, input().split())
    taxi_y -= 1
    taxi_x -= 1

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for _ in range(M):
        dep_y, dep_x, des_y, des_x = map(int, input().split())
        temp_board[dep_y - 1][dep_x - 1] = (des_y - 1, des_x - 1)

    # for t in temp_board:
    #     print(t)
    # print()

    def search_passenger(ty, tx, dis):  # 현재 택시 좌표, 목적지 좌표, 이동 거리 반환
        q = deque()
        q.append([ty, tx, dis])
        visited = [[0] * N for _ in range(N)]
        visited[ty][tx] = 1

        result = []

        while q:
            y, x, dis = q.popleft()

            if temp_board[y][x] and board[y][x] != 2:
                des_y, des_x = temp_board[y][x]
                result.append((y, x, des_y, des_x, dis))

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx, dis + 1])

        if result:
            result.sort(key=lambda x: (x[4], x[0], x[1]))
            return result[0]
        else:
            return (0, 0, 0, 0, -1)

    def move_destination(ty, tx, des_y, des_x, dis):  # 현재 택시 좌표, 이동한 거리 반환
        q = deque()
        q.append([ty, tx, dis])
        visited = [[0] * N for _ in range(N)]
        visited[ty][tx] = 1

        while q:
            y, x, dis = q.popleft()

            if y == des_y and x == des_x:
                return (y, x, dis)

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx, dis + 1))

        return (y, x, 0)

    def is_end():
        for i in range(N):
            for j in range(N):
                if temp_board[i][j]:
                    return False

        return True

    # 가장 가까운 승객 탐색
    while True:
        if is_end():
            return answer

        # print("#", taxi_y, taxi_x, answer)
        taxi_y, taxi_x, des_y, des_x, dis = search_passenger(taxi_y, taxi_x, 0)
        temp_board[taxi_y][taxi_x] = 0
        # print("@", taxi_y, taxi_x, des_y, des_x, dis)

        if dis == -1 or answer < dis:
            return -1
        else:
            answer -= dis

        # print("##", taxi_y, taxi_x, des_y, des_x, answer)
        taxi_y, taxi_x, dis = move_destination(taxi_y, taxi_x, des_y, des_x, 0)
        # print("@@", taxi_y, taxi_x, dis)

        if dis:
            if answer < dis:
                return -1
            answer -= dis
            answer += dis * 2
        else:
            return -1

        # for t in temp_board:
        #     print(t)
        # print()


if __name__ == "__main__":
    print(solution())
