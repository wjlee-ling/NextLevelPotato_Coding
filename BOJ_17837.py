def solution():
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    loc_board = [[[] for _ in range(N)] for _ in range(N)]
    pieces = []
    for i in range(K):
        row, col, d = map(int, input().split())
        row -= 1
        col -= 1
        d -= 1
        pieces.append([row, col, d])
        loc_board[row][col].append([i, d])

    #  →, ←, ↑, ↓
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    # for p in loc_board:
    #     print(p)
    # print()

    for answer in range(1, 1001):
        # print("@@@@@@", answer)
        for i, piece in enumerate(pieces):
            row, col, d = piece

            nrow = row + dy[d]
            ncol = col + dx[d]

            for idx in range(len(loc_board[row][col])):
                if loc_board[row][col] and loc_board[row][col][idx][0] == i:
                    break

            if 0 <= nrow < N and 0 <= ncol < N:
                if board[nrow][ncol] == 0:  # 흰색칸
                    if loc_board[row][col]:
                        loc_board[nrow][ncol].extend(loc_board[row][col][idx:])
                        loc_board[row][col] = loc_board[row][col][:idx]

                        for p in loc_board[nrow][ncol]:
                            pieces[p[0]] = [nrow, ncol, p[1]]

                if board[nrow][ncol] == 1:  # 빨간색칸
                    if loc_board[row][col]:
                        loc_board[nrow][ncol].extend(loc_board[row][col][idx:][::-1])
                        loc_board[row][col] = loc_board[row][col][:idx]

                        for p in loc_board[nrow][ncol]:
                            pieces[p[0]] = [nrow, ncol, p[1]]

                if board[nrow][ncol] == 2:  # 파란색칸
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    elif d == 3:
                        d = 2

                    nrow = row + dy[d]
                    ncol = col + dx[d]
                    loc_board[row][col][idx][1] = d
                    pieces[loc_board[row][col][idx][0]][2] = d
                    if not (0 <= nrow < N and 0 <= ncol < N) or board[nrow][ncol] == 2:
                        continue
                    else:
                        if board[nrow][ncol] == 0:  # 흰색칸
                            if loc_board[row][col]:
                                loc_board[nrow][ncol].extend(loc_board[row][col][idx:])
                                loc_board[row][col] = loc_board[row][col][:idx]

                                for p in loc_board[nrow][ncol]:
                                    pieces[p[0]] = [nrow, ncol, p[1]]

                        if board[nrow][ncol] == 1:  # 빨간색칸
                            if loc_board[row][col]:
                                loc_board[nrow][ncol].extend(loc_board[row][col][idx:][::-1])
                                loc_board[row][col] = loc_board[row][col][:idx]

                                for p in loc_board[nrow][ncol]:
                                    pieces[p[0]] = [nrow, ncol, p[1]]

            else:  # 체스판을 벗어나는 경우 (파란색칸과 같음)
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2

                nrow = row + dy[d]
                ncol = col + dx[d]
                loc_board[row][col][idx][1] = d
                pieces[loc_board[row][col][idx][0]][2] = d
                if not (0 <= nrow < N and 0 <= ncol < N) or board[nrow][ncol] == 2:
                    pass
                else:
                    if board[nrow][ncol] == 0:  # 흰색칸
                        if loc_board[row][col]:
                            loc_board[nrow][ncol].extend(loc_board[row][col][idx:])
                            loc_board[row][col] = loc_board[row][col][:idx]

                            for p in loc_board[nrow][ncol]:
                                pieces[p[0]] = [nrow, ncol, p[1]]

                    if board[nrow][ncol] == 1:  # 빨간색칸
                        if loc_board[row][col]:
                            loc_board[nrow][ncol].extend(loc_board[row][col][idx:][::-1])
                            loc_board[row][col] = loc_board[row][col][:idx]

                            for p in loc_board[nrow][ncol]:
                                pieces[p[0]] = [nrow, ncol, p[1]]

            if len(loc_board[nrow][ncol]) >= 4:
                # print(loc_board[nrow][ncol])
                return answer

            # print("@", i)
            # for l in loc_board:
            #     print(l)
            # print()

    return -1


if __name__ == "__main__":
    print(solution())
