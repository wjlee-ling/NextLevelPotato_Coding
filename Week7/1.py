'''
1,2,...,N개의 이벤트
M명의 사용자가 이벤트를 실행한 내역을 보고 가장 자주 실행한 이벤트 찾기
- 한 사람이 같은 이벤트 여러 번 실행해도 여러번 세어준다
- 가장 많이 실행한 이벤트가 여러 개라면, 큰 번호 먼저 출력
'''
from collections import defaultdict
#import sys
#sys.stdin = open('./input.txt', 'r')

# 1. 입력 받기
N, M = map(int, input().split())
cnt = defaultdict(int)

for _ in range(M):
    arr = list(map(int, input().split()))[1:]
    for i in arr:
        cnt[i] += 1
#print(cnt)

# 2. 개수 -> 이벤트 번호 큰 순서로 정렬
cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse= True)
#print(cnt)

temp = cnt[0][1]
print(cnt[0][0], end=' ')

for i in range(1, len(cnt)):
    if cnt[i][1] != temp:
        break
    print(cnt[i][0], end=' ')

