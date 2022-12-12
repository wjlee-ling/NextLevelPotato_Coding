'''
이진탐색
'''

def solution(stones, k):
    answer = 0
    left, right = min(stones), max(stones) 
    
    while left <= right:
        cnt = 0
        mid = (left + right)//2
        for s in stones: # mid명이 건널 수 있는 지를 확인
            if s-mid <= 0: # 0이 연속적으로 나오는 경우
                cnt += 1
            else:
                cnt = 0 # 0이 연속적으로 안 나오면 초기화
            if cnt >= k: # 더 이상 건널 수 없는 경우
                break
        if cnt < k: # 더 많이 건널 수 있음
            #answer = mid
            left = mid + 1
        else: # 덜 건너야 함
            answer = mid
            right = mid -1
            
    return answer

'''
# *** 오답(정확성 테스트 통과, 효율성 테스트 통과 못함)***
디딤돌을 밟을 때마다 1씩 줄어들고 숫자가 0이 되면 밟을 수 없음
그 다음 디딤돌로 여러 칸 건너뛰기 가능

stones: 디딤돌에 적힌 숫자
k: 한 번에 건너뛸 수 있는 최대 칸 수
최대 몇 명까지 징검다리를 건널 수 있는 가

def check(stones): # 연달아 0인 원소의 개수 반환
    cnt, tmp = 0, 0 # 연속된 0의 개수의 최대값
    for i in range(len(stones)):
        if stones[i] <= 0:
            tmp += 1
            cnt = max(cnt, tmp)
            continue
        else:
            tmp = 0
    return cnt

def solution(stones, k):
    answer = 0
    while True:
        num = check(stones)
        if num >= k:
            return answer
            break
        else:
            stones = [x-1 for x in stones]
            answer += 1
'''