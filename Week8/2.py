'''
몇 명의 신선이 자신의 뒤통수를 보는 가
a가 b를 보기 위해서는 a<b이고 
a와 b 사이 봉우리는 a의 높이보다 작아야 한다.(a봉우리가 b봉우리보다 높을 필요는 없다)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
if arr[0] > arr[1]:
	answer = [0,1]
else:
	answer = [0,0]

for b in range(2, len(arr)): 
	cnt = 1
	for a in range(0, b-1):
		if max(arr[a+1:b]) < arr[a]:
			cnt += 1
	answer.append(cnt)
	
print(*answer)

''' # 3, 4 4 4 같은 케이스는 틀리는 거 아님?
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []

for i in range(N):
	print(len(stack), end=' ')
	#print(stack)
	while stack and stack[-1] <= arr[i]:
			stack.pop()
	#print(stack)
	stack.append(arr[i])
	#print("i: ", i, " stack: ", stack)
'''
