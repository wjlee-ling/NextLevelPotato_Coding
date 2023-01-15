'''
tan에서 k개를 담을 때
크기 별로 분류했을 때 종류의 수를 최소화

종류의 수를 return
'''
from collections import Counter 

def solution(k, tan):
    #print(sorted(Counter(tan).items(), reverse=True, key=lambda x: x[1]))
    cnt = 0
    answer = 0
    for size, num in sorted(Counter(tan).items(), reverse=True, key=lambda x: x[1]):
        if cnt >= k:
            break
        cnt += num
        answer += 1
    return answer