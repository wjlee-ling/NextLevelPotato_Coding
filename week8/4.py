# 시간 부족 미해결

# 1번 도시에서 start
# 최대로 쓰레기를 담을 수 있어야 함


import sys

def input():
	return sys.stdin.readline().rstrip()

# 첫번째 줄 입력 : 도시 수, 쓰레기 봉투 용량
N, K = map(int, input().split())
# N-1 줄 입력 : 서로 이어져있는 두 도시 번호
for _ in range(N-1):
	a, b = map(int, input().split())
	print(a, b)
# 마지막 줄 입력 : 도시에 쌓인 쓰레기 양
garbages = list(map(int, input().split()))