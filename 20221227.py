'''
n칸에 1칸 또는 2칸으로 도달하는 방법의 수 % 1234567
DP
1, 2, 3(1+1+1, 2+1, 1+2), 4(1+1+1+1, 2+2, 2+1+1 *3)
'''

def solution(n):
    if n<3:
        return n
    dp =[0]*(n+1)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[n]%1234567