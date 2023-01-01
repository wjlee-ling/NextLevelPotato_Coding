'''
숫자 N과 사칙연산을 최소 몇 개 사용해서 number을 표현할 수 있는 가
N = 2일 때 22/2 처럼 22, 222.. 도 가능 
만약 연속이 안 됐다면 number%N + number//N이었을 텐데

DP인 것 같은데 시작 케이스를 N을 기준으로 해야 할지, number을 기준으로 할 지(작은 문제 정의하기)
=> N을 1개 사용, 2개 사용, 3개 사용.. 해서 표현할 수 있는 경우
=> 1부터 9 사이의 N을 사용해서 만들 수 있는 수 집합을 미리 구하고, number이 처음 나올 때를 리턴 
'''

def solution(N, number):
    answer = -1
    dp =  [set() for i in range(9)] # N을 i번 사용해서 표현할 수 있는 숫자를 담는 리스트
    # [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    
    for i in range(1,9): # i는 N의 개수
        num = int(str(N)*i) # {N}, {NN}, {NNN}...
        dp[i].add(num)
        for j in range(i//2+1):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op2 - op1)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                    if op1 != 0:
                        dp[i].add(op2 // op1)
        if number in dp[i]:
            return i
    return -1