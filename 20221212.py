'''
길이가 같은 두 큐
작업 1회 : 한 번 pop하고 insert함

idea: 
q1, q2의 합을 비교하면서 큰 데서 작은 데로 원소 이동 (그리디)

detail:
1. deque의 popleft 사용
2. 최대 횟수를 len(q1)*3로 지정
3. q1의 합을 L, q2의 합을 R이라고 지정해서 sum을 매번하지 않도록
'''
from collections import deque

def solution(q1, q2):
    q1, q2 = deque(q1), deque(q2)
    L, R = sum(q1), sum(q2)
    answer = 0
    cnt = len(q1)*3

    while answer <= cnt:
        if L == R:
            return answer
        elif L < R: #q2에서 q1으로 옮기기
            tmp = q2.popleft()
            q1.append(tmp)
            R -= tmp
            L += tmp
            answer += 1
        elif L > R:
            tmp = q1.popleft()
            q2.append(tmp)
            R += tmp
            L -= tmp
            answer += 1
    return -1


''' #예전 풀이
from collections import deque

def solution(q1, q2):
    '''
    q1, q2 원소의 합이 동일하게
    pop, insert를 묶어서 한 번의 작업으로 친다
    총 작업을 몇 번 수행했는 지 return
    '''
    q1, q2 = deque(q1), deque(q2)
    L, R = sum(q1), sum(q2)
    
    # 어떤 방법으로도 L, R 같아지지 않는 경우
    if (L+R)% 2 != 0:
        return -1
    
    # while문으로 하면 [1,1],[1,2]와 같은 케이스에서 무한 루프
    # for문으로 횟수를 지정해야 하는데 len(q1)*2로 하면 1번 케이스 안됨
    for cnt in range(len(q1)*3):
        if L == R:
            return cnt
        elif L > R:
            tmp = q1.popleft()
            q2.append(tmp)
            R += tmp
            L -= tmp
        elif L < R:
            tmp = q2.popleft()
            q1.append(tmp)
            R -= tmp
            L += tmp
    return -1 # [1,1], [1,5]와 같은 케이스
'''