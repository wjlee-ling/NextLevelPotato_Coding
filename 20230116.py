'''
인접한 두 집을 털면 경보 울림

money : 각 집에 있는 돈이 담긴 배열
도둑이 훔칠 수 있는 돈의 최댓값을 return

첫 접근법:
OXOX
OXXO 집이 짝수 개인 경우 X 연달아
OXOXO
이거 아님!! 첫번째 집과 마지막 집은 이웃임 -> 어떻게 처리?

DP인지도 몰랐다

1. 원형이 아닌 일자 형태일 경우
dp[i] = max(dp[i-2] + money[i], dp[i-1])

2. 여기서 맨 앞을 털 떄, 맨 뒤를 털 때 나눠서
'''

def solution(money):
    answer = 0
    tmp = -float('inf')
    
    # 1. 첫 집을 무조건 터는 경우
    dp = [0]*(len(money))
    dp[0] = money[0]
    dp[1] = max(money[0], money[1]) # 첫 집을 무조건 털면 두 번째 집은 자동으로 못 터는 거 아닐까?
                                    # -> dp[2], dp[3]에서 고려해주기 위해
    for i in range(2, len(money)-1):
        dp[i] =  max(dp[i-2] + money[i], dp[i-1])
    #print(dp) #[1, 2, 4, 0]
        
    # 2. 마지막 집을 무조건 터는 경우
    dp2 = [0]*(len(money))
    dp2[0] = 0
    dp2[1] = money[1] # 첫 집은 방문 안함
    for i in range(2, len(money)):
        dp2[i] =  max(dp2[i-2] + money[i], dp2[i-1])
    print(dp2) #[0, 2, 3, 3]
    
    return max(max(dp), max(dp2))
