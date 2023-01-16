# 인접한 집을 털면 경보가 울림
# [1, 2, 3, 1] 에서 idx 0과 idx -1은 인접함
## 첫번째 집을 털 경우와 첫번째 집을 털지 않을 경우로 분리

# dp[i] 값
## (i-2)번째 집을 털고 현재 i번째 집을 터는경우 (dp[i-2] + money[i])
## (i-1)번째 집을 턴 경우(i번째 집 못텀) (dp[i-1])


def solution(money):
    """
    Args:
        money (List[int]) : 집에 있는 돈이 담긴 배열
    Returns:
        훔칠 수 있는 돈의 최댓값
    """
    # 첫번째 집을 터는 경우
    dp_1 = [0]*len(money)
    dp_1[0] = money[0]
    
    for i in range(1, len(money) - 1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + money[i])
    
    # 첫번째 집을 털지 않는 경우
    dp_2 = [0]*len(money)
    
    for i in range(1, len(money)):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + money[i])
    
    return max(dp_1[-2], dp_2[-1])