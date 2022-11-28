'''
구름 숫자: 알파벳 소문자를 사용해 숫자 표기
중복되는 알파벳이 있으면 합친다

구름 숫자를 보고 기존 숫자로 바꿔라(여러 개로 가능하면 길이가 가장 긴 값으로)
qwer -> qw we er 
'''
import sys
input = sys.stdin.readline

arr = ['ze', 'qw', 'as', 'zx', 'we', 'sd', 'xc', 'er', 'df', 'cv']
N = int(input())
num = list(input())
#print(N, num)

answer = ''
for i in range(len(num)-1):
	tmp = num[i]+ num[i+1]
	if tmp in arr:
		answer += str(arr.index(tmp))

print(int(answer))
		
		
		
