'''
n명을 입국심사를 받아야 하고, len(times)가 입국심사대

시간의 최소, 최대 범위를 구하고 중간 값이 n명을 심사 할 수 있는 시간인지 확인하며 이분 탐색을 진행
=> 걸리는 시간(mid)을 구하는데 이분 탐색을 사용하라

총 걸린 시간이 28분이었는데 times가 [7,10]이면
28//7 + 28//10 = 4 + 2 = 6명을 검사할 수 있었음 
'''
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n
    while left <= right:
        mid = (left + right) //2 # 구하려는 값이 mid보다 큰 지 작은 지 체크
        tmp = 0 # 심사관이 mid 분 동안 심사한 사람의 수
        for time in times:
            tmp += mid // time
                
        if tmp >= n: # 더 적은 시간도 가능한 지 체크
            answer = mid
            right = mid-1
        elif tmp < n: # 더 많은 시간 필요
            left = mid +1
    
    return answer

# https://happy-obok.tistory.com/10