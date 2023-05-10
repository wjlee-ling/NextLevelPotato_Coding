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
        y, x = N // 2, N // 2
        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]
        depth = 0

        while True:
            for i in range(4):
                if i % 2 == 0:
                    depth += 1
                for j in range(depth):
                    y += dy[i]
                    x += dx[i]
                    indices.append((y, x))
                    if y == 0 and x == 0:
                        return

    def magic(d, dist):
        y, x = N // 2, N // 2
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        for i in range(dist):
            y += dy[d]
            x += dx[d]
            if y < 0 or y >= N or x < 0 or x >= N:
                break
            board[y][x] = 0

        fill_blank()
        while boom():
            fill_blank()
        grouping()

    def fill_blank():
        blanks = deque()
        for y, x in indices:
            if board[y][x] == 0:
                blanks.append((y, x))
            elif board[y][x] > 0 and blanks:
                nx, ny = blanks.popleft()
                board[nx][ny] = board[y][x]
                board[y][x] = 0
                blanks.append((y, x))

    def boom():
        global answer
        visited = deque()
        cnt = 0
        num = -1
        flag = False
        for y, x in indices:
            if num == board[y][x]:
                visited.append((y, x))
                cnt += 1
            else:
                if cnt >= 4:
                    answer += num * cnt
                    flag = True

                while visited:
                    nx, ny = visited.popleft()
                    if cnt >= 4:
                        board[nx][ny] = 0

                num = board[y][x]
                cnt = 1
                visited.append((y, x))

        return flag

    def grouping():
        cnt = 1
        tmpy, tmpx = indices[0]
        num = board[tmpy][tmpx]
        nums = []

        for i in range(1, len(indices)):
            y, x = indices[i][0], indices[i][1]
            if num == board[y][x]:
                cnt += 1
            else:
                nums.append(cnt)
                nums.append(num)
                num = board[y][x]
                cnt = 1

        idx = 0
        for y, x in indices:
            if not nums:
                break
            board[y][x] = nums[idx]
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
