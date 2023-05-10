"""
21611. 마법사 상어와 블리자드
"""


from collections import deque


def solution():
    global answer
    answer = 0
    N, M = map(int, input().split())
    board = []

    def indexing():
        x, y = N // 2, N // 2
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        depth = 0

        while True:
            for i in range(4):
                if i % 2 == 0:
                    depth += 1
                for j in range(depth):
                    x += dx[i]
                    y += dy[i]
                    indices.append((x, y))
                    if x == 0 and y == 0:
                        return

    def magic(d, dist):
        x, y = N // 2, N // 2
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(dist):
            x += dx[d]
            y += dy[d]
            if x < 0 or x >= N or y < 0 or y >= N:
                break
            board[x][y] = 0

        fill_blank()
        while boom():
            fill_blank()
        grouping()

    def fill_blank():
        blanks = deque()
        for x, y in indices:
            if board[x][y] == 0:
                blanks.append((x, y))
            elif board[x][y] > 0 and blanks:
                nx, ny = blanks.popleft()
                board[nx][ny] = board[x][y]
                board[x][y] = 0
                blanks.append((x, y))

    def boom():
        global answer
        visited = deque()
        cnt = 0
        num = -1
        flag = False
        for x, y in indices:
            if num == board[x][y]:
                visited.append((x, y))
                cnt += 1
            else:
                if cnt >= 4:
                    answer += num * cnt
                    flag = True

                while visited:
                    nx, ny = visited.popleft()
                    if cnt >= 4:
                        board[nx][ny] = 0

                num = board[x][y]
                cnt = 1
                visited.append((x, y))

        return flag

    def grouping():
        cnt = 1
        tmpx, tmpy = indices[0]
        num = board[tmpx][tmpy]
        nums = []

        for i in range(1, len(indices)):
            x, y = indices[i][0], indices[i][1]
            if num == board[x][y]:
                cnt += 1
            else:
                nums.append(cnt)
                nums.append(num)
                num = board[x][y]
                cnt = 1

        idx = 0
        for x, y in indices:
            if not nums:
                break
            board[x][y] = nums[idx]
            idx += 1
            if idx == len(nums):
                break

    board = [list(map(int, input().split())) for _ in range(N)]
    indices = deque()
    indexing()
    # for i in indices:
    #     print(i)
    # print()

    for _ in range(M):
        d, s = map(int, input().split())
        magic(d - 1, s)

    return answer


if __name__ == "__main__":
    print(solution())
