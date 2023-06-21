"""
14889. 스타트와 링크
"""


def solution():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    global answer
    answer = float("inf")
    visited = [0] * N

    def solve(member, idx):
        global answer
        if member == N // 2:
            team1, team2 = 0, 0
            for i in range(N):
                for j in range(N):
                    if visited[i] == 1 and visited[j] == 1:
                        team1 += S[i][j]
                    elif visited[i] == 0 and visited[j] == 0:
                        team2 += S[i][j]

            answer = min(answer, abs(team1 - team2))
            return

        for i in range(idx, N):
            if visited[i] == 0:
                visited[i] = 1
                solve(member + 1, i + 1)
                visited[i] = 0

    solve(0, 0)

    return answer


if __name__ == "__main__":
    print(solution())
