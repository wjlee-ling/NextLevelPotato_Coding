## ex.1
"""
try 1: bigram으로 자르기
"""
_ = input()
s = input()
num2str = {'1': 'qw', '2':'as', '3':'zx', '4': 'we', '5':'sd', '6':'xc', '7':'er', '8':'df', '9':'cv', '0':'ze'}

answer = ''
for i in range(len(s)-1):
	bigram = s[i:i+2]
	for k,v in num2str.items():
		if v == bigram:
			answer += k 
print(answer)

## ex.2

N = int(input())
heights = list(map(int, input().split()))
trends = []
for i in range(len(heights)-1):
	if heights[i] < heights[i+1]:
		trends.append('up')
	elif heights[i] > heights[i+1]:
		trends.append('down')
	else:
		trends.append('even')
		
	
"""
try 1: DP

"""
# prev_highest, prev_h = heights[0], heights[0] 
# idx_highest = 0
# answers = [0]
# print(0, end=' ')
# for idx, h in enumerate(heights[1:], start=1):
# 	if prev_h < h:
# 		# 직전 봉아리 보다 높음
# 		if prev_highest == h:
# 			# 이전 최고봉이랑 같음
# 			answer = len([x for x in heights[idx_highest:idx] if x >= prev_h])
# 			idx_highest = idx
			
# 		elif prev_highest < h:
# 			# 새 최고봉
# 			answer = 0
# 			prev_highest = h
# 			idx_highest = idx
# 		else: 
# 			# 이전 최고봉보다는 낮음
# 			answer = len([x for x in heights[idx_highest:idx] if x >= prev_h])
				
# 	elif prev_h == h:
# 		answer = answers[-1]+1
		
# 	elif prev_h > h:
# 		answer = len([x for x in heights[idx_highest:idx] if x >= prev_h])
		
# 	answers.append(answer)
# 	prev_h = h
# 	print(answer, end=' ')


## ex.3

"""
try 1: 가설 1) 서로 길이가 비슷한애들끼리 했을 때 최대?
N이 매우 클 수 있으므로 sorted 대신 heapq 사용

반례 5,5, 6,7 => 순서대로 묶으면 안됨
정사각형도 직사각형??

try 2 : 바보같이 lens = list(set(sticks)) 했었음.
"""
import heapq

_ = input()
sticks = list(map(int, input().split()))
lens = [stick*(sticks.count(stick)//2) for stick in list(set(sticks))]

heapq.heapify(lens)

answer = 0
while len(lens) >= 2:
	a = lens.pop(0)
	heapq.heapify(lens)
	b = lens.pop(0)
	answer += a*b
	
print(answer)




