# 각각의 큐의 합을 같게 만들어야한다.
## 즉, 각각의 큐의 합은 전체 합의 1/2

# 각 큐의 합 중에 큰 큐가 pop하여 다른 queue에 insert한다.

# loop문 종료 조건은 한 큐가 다 나갔다가 다시 원상태로 돌아올 때 까지
## 3 * len(queue)

from collections import deque

def solution(queue1, queue2):
    """
    Args:
        queue1 (List) : 정수배열
        queue2 (List) : 정수배열
    Returns:
        각 큐의 원소의 합을 같게 만들기 위해 필요한 최소 작업 횟수
        불가능한 경우 -1
    """
    
    q1, q2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(q1), sum(q2)
    cnt = 0
    goal = (sum_q1 + sum_q2) / 2
    
    while cnt <= len(queue1)*3 :
        if sum_q1 == sum_q2:
            return cnt
        
        if sum_q1 > sum_q2:
            temp = q1.popleft()
            q2.append(temp)
            sum_q1 -= temp
            sum_q2 += temp
            cnt += 1
        elif sum_q1 < sum_q2:
            temp = q2.popleft()
            q1.append(temp)
            sum_q1 += temp
            sum_q2 -= temp
            cnt += 1

    return -1