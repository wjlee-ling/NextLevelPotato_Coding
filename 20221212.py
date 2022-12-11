def solution(queue1, queue2):
    # another try
    # either queue1 or queue2 
    from collections import deque
    target = (sum(queue1) + sum(queue2)) / 2
    if int(target) - target != 0.:
        return -1
    else:
        queue1, queue2 = map(deque, (queue1, queue2))
        target = int(target)
    answer = 0
    s = sum(queue1)
    l = len(queue1)
    while s != target:
        if s > target:
            ele = queue1.popleft()
            queue2.append(ele)
            s -= ele
        else:
            ele = queue2.popleft()
            queue1.append(ele)
            s += ele
        answer +=1
        if answer > 3 *l:
            return -1
    return answer
        
    
#     """
#     1st try: queue 하나가 sum/2 -> success
#     """
#     from collections import deque
#     answer = 0
#     target = (sum(queue1) + sum(queue2)) / 2
#     if target != int(target):
#         return -1
#     else:
#         target = int(target)
#     q1, q2 = deque(queue1), deque(queue2)
#     s = sum(q1)
#     limit = len(q1) + len(q2) * 2
#     i = 0
#     while s != target:
#         if s < target:
#             new = q2.popleft()
#             q1.append(new)
#             s += new
#         elif s > target:
#             old = q1.popleft()
#             q2.append(old)
#             s -= old
#         answer += 1    
#         if s == target:
#             break
#         if  len(q1) == 0:
#             return -1
#         i+=1
#         if i == limit:
#             return -1
#     return answer
