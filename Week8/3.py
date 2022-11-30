'''
N개의 직선 막대기. 네 개의 막대기로 하나의 직사각형을 만든다.
막대기를 가지고 만들 수 있는 직사각형 넓이의 합이 최대가 되게

같은 직선이 모두 2개씩이 아니라면?
'''
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
lines = list(map(int, input().split()))

# 1. 막대기 쌍 처리
pair = [] # lines 후처리 (1, 홀수 처리)
counter = Counter(lines)
#print(counter)
for line in counter.keys():
	while counter[line] > 1:
		counter[line] -= 2
		pair.append(line)
#print(pair)

# 2. 직사각형들 넓이 계산
pair.sort(reverse=True)
ans = 0
for i in range(0, len(pair)-1, 2):
    ans += pair[i] * pair[i+1]

print(ans)

'''
from collections import Counter
import sys
input = sys.stdin.readline

def calculate():
	N = int(input())
	line = list(map(int, input().split()))
	line = [x for x in line if line.count(x) >= 2 ] # 1. 직선이 하나인 경우 제거
	if line == []:
		print(0)
		return 0
	for x in line: # 2. 직선이 3 이상 홀수 개라면 짝수 개로
		if line.count(x) % 2 != 0:
			line.remove(x)
	# 3. 원소 두 개를 하나로 줄이기 
	line_arr = []
	count = Counter(line)
	for i in count:
		for _ in range(count[i]//2):
			line_arr.append(i)

	#print(line_arr)
	if line_arr == []: #  직사각형을 아예 못 만드는 경우에는?
		print(0)
		return 0
	
	ans = 0
	line_arr = sorted(line_arr)
	for i in range(0, len(line_arr)-1, 2):
		ans += line_arr[i]*line_arr[i+1]	
	print(ans)

calculate()
'''

