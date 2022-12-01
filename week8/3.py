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

while max_heap and len(max_heap) % 2 == 0:
	a = - heapq.heappop(max_heap)
	b = - heapq.heappop(max_heap)
	answer += a*b

print(answer)


###################################################################
# 네 개의 막대기 쌍이 있으면 항상 길이가 짧은 막대기 쌍 두 개와 길이가 긴 막대기 쌍 두 개를 짝 지어주는 것이 최적

import sys
def input():
	return sys.stdin.readline().rstrip()

# 첫번째 줄 입력: 막대기 수
N = int(input())
# 둘째 줄 입력: 막대기의 길이
sticks = list(map(int, input().split()))

cnt = [0 for _ in range(1000001)]
pair = []
for stick in sticks:
	cnt[stick] += 1

for length in range(1, 1000001):
	while cnt[length] > 1:
		cnt[length] -= 2
		pair.append(length)

pair.sort(reverse=True)
answer = sum(pair[i-1] * pair[i] for i in range(1, len(pair), 2))
print(answer)