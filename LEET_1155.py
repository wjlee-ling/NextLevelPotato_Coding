class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                for v in range(1, min(j, k) + 1):
                    # n-1개의 주사위로 target - 나올 수 있는 눈의 값의 경우를 다 더해주면 n개의 주사위로 target 값이 나올 수 있는 경우가 됨
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - v]) % MOD

        print(dp)

        return dp[n][target]


if __name__ == "__main__":
    solution = Solution()
    n = [1, 2, 30]
    k = [6, 6, 30]
    target = [3, 7, 500]
    output = [1, 6, 222616187]

    for n1, k1, t in zip(n, k, target):
        print(solution.numRollsToTarget(n1, k1, t))
