from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1] # tip: answer = [] 한 뒤 마지막에 빈 list면 [-1] 리턴하지 말고 선언할 때 부터
    max_gap = -1 #최대 차이가 나는 gap 구하기 위한 temp
    
    for combination in combinations_with_replacement(range(11), n):
        lion_info = [0]*11 #lion의 info_list
        # 0~10까지의 수 n개 중복조합으로 뽑기(전체 경우의 수 구하기)
        for c in combination: # 중복 조합 1개의 경우
            lion_info[10-c] += 1
        
        # 점수 계산
        lion_score, peach_score = 0, 0 # 라이언과 어피치의 점수
        for i in range(11):
            if info[i] == 0 and lion_info[i] == 0:
                continue
            elif info[i] >= lion_info[i]: 
                peach_score += (10-i)
            else:
                lion_score += (10-i) 
        if lion_score <= peach_score:
            continue
        else:
            gap = lion_score - peach_score
            if gap > max_gap:
                max_gap = gap
                answer = lion_info
    return answer


#-----------------------------------------#
from collections import deque

def bfs(n, info):    
    answer = [-1]
    q = deque([(0, [0]*11)])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0): # 둘 다 0점이면 안됨
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap: # = 들어가면 안됨 
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                answer= arrow # 최대점수차를 내는 화살상황 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏜 경우
            continue
        
        elif focus == 10:  # 종료조건 3) 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((10, tmp))
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return answer

def solution(n, info):
    answer = bfs(n, info)
    return answer