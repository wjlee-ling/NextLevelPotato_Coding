
# 테스트케이스 timeout 

# target의 idx가 0이면 0
# target의 idx가 0이 아니면
## idx값 크기만큼 돌면서 idx-i가 그 사이 값들보다 커야함


import sys

def input():
	return sys.stdin.readline().rstrip()

# 첫 번째 입력: 봉우리의 수
N = int(input())
# 두 번째 입력: 봉우리의 높이가 왼쪽에서부터 순서대로 입력
m_list = list(map(int, input().split()))

answer = []

for i in range(len(m_list)):
	if i == 0:
		answer.append("0")
	else:
		count = 0
		for j in range(i):
			target = m_list[j]
			if j-i == 1:
				count += 1
			else:
				middle = m_list[j+1: i]
				if middle:
					max_middle = max(middle)
					if max_middle < target:
						count += 1
		count += 1
		answer.append(str(count))

temp = " ".join(answer)
print(temp)