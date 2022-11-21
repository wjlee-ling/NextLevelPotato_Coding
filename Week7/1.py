# Testcase 5/7/15/16/17/18/19 → Fail


# 사용자들이 취할 수 있는 이벤트 개수 N
# 사용자의 수 M

# 목표: M명의 사용자들이 가장 자주 실행했던 이벤트

# 이벤트 별 호출 횟수 딕셔너리를 만든 뒤 최대값과 일치하는 key들을 출력

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
event_dict = defaultdict(int)

for _ in range(M):
	user_event = input()
	temp = user_event.split(" ")[1:]
	for k in temp:
		event_dict[k] += 1

max_event_key = [k for k, v in event_dict.items() if max(event_dict.values()) == v] # ❌ 시간초과 발생 부분

print(" ".join(sorted(max_event_key, reverse=True)))



###################################################
# Testcase 6/8 → Fail

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
event_dict = defaultdict(int)

for _ in range(M):   # ❌ {'1': 4, '2': 4, '3': 4, '4': 4}) 🙄왜 key값이 int여야 할까요?
	user_event = input()
	temp = user_event.split(" ")[1:]
	for k in temp:
		event_dict[k] += 1

# 정렬하고 첫 번째 값의 key값 먼저 출력
sorted_event_dict = sorted(event_dict.items(), key= lambda x: (x[1], x[0]), reverse=True)
print(sorted_event_dict[0][0], end = " ")

# 첫 번째 값과 value가 같은 key 값 추출
idx = 0
while True:
	if idx == len(sorted_event_dict) - 1:
		break
	if sorted_event_dict[idx][1] == sorted_event_dict[idx+1][1]:
		print(sorted_event_dict[idx+1][0], end= " ")
		idx += 1
	else:
		break



###################################################
# Testcase 6/8 → Fail

import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
event_dict = defaultdict(int)

for _ in range(M): # {1: 4, 2: 4, 3: 4, 4: 4})
	user_event = list(map(int, input().split()))
	
	for k in user_event[1:]:
		event_dict[k] += 1

# 정렬하고 첫 번째 값의 key값 먼저 출력
sorted_event_dict = sorted(event_dict.items(), key= lambda x: (x[1], x[0]), reverse=True)
print(sorted_event_dict[0][0], end = " ")

# 첫 번째 값과 value가 같은 key 값 추출
idx = 0
while True:
	if idx == len(sorted_event_dict) - 1:
		break
	if sorted_event_dict[idx][1] == sorted_event_dict[idx+1][1]:
		print(sorted_event_dict[idx+1][0], end= " ")
		idx += 1
	else:
		break