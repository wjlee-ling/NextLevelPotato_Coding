# test case 1,2,4,7 빼고 다 틀림

# 넓이 합이 최대가 되려면 우선 큰 것끼리 곱해줘야 함
## 그리고 해당 값이 2개 씩 있어야 함
### 2개인 것들만 따로 추리다음에 면적 곱해서 더해주기

import sys
import heapq

def input():
	return sys.stdin.readline().rstrip()

# 첫번째 줄 입력: 막대기 수
N = int(input())
# 둘째 줄 입력: 막대기의 길이
s_list = list(map(int, input().split()))
final_list = []
answer = 0

for i in set(s_list):
	target = s_list.count(i)
	if target % 2 == 0:
		temp = [i] * (target // 2)
		final_list.extend(temp)

max_heap = []
for item in final_list:
	heapq.heappush(max_heap, -item)

while len(max_heap) > 0 and len(max_heap) % 2 == 0:
	a = - heapq.heappop(max_heap)
	b = - heapq.heappop(max_heap)
	answer += a*b

print(answer)