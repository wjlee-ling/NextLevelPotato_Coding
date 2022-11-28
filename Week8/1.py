'''
구름 숫자: 알파벳 소문자를 사용해 숫자 표기
중복되는 알파벳이 있으면 합친다

구름 숫자를 보고 기존 숫자로 바꿔라(여러 개로 가능하면 길이가 가장 긴 값으로)
qwer -> qw we er 

idea: 세개 이상이 이어진 경우
qr -> ('qw', 'we', 'er')  147
ad -> ('as', 'sd', 'df') 258
zc -> ('zx', 'xc', 'cv') 369
'''
import sys
input = sys.stdin.readline

arr = ['', 'qw', 'as', 'zx', 'we', 'sd', 'xc', 'er', 'df', 'cv', 'ze']
N = int(input())
num = list(input())
'''
tmp = []
for i in range(1, len(arr)):
	for j in range(1, len(arr)):
		for k in range(1, len(arr)): # i-> j -> k
			if arr[i][1] == arr[j][0] and arr[j][1] == arr[k][0]:
				tmp.append((arr[i], arr[j], arr[k]))
print(tmp)
'''
		
answer = ''
exp = ['qr', 'ad', 'zc']
exp_num = ['147', '258', '369']
for i in range(len(num)-1):
	tmp = num[i]+ num[i+1]
	if tmp in arr:
		answer += str(arr.index(tmp))
	elif tmp in exp:
		answer += exp_num[exp.index(tmp)]

print(int(answer))
		
		
		