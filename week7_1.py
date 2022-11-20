"""
UXUI 디자이너 (별 1)

"""
4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 3

3

4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4

4 3 2 1


'''
Counter로 계산후 most_common() 사용 -> 10, 17, 18, 19 fail
'''

from collections import Counter

N,M = map(int, input().split())
c = Counter()
for _ in range(M):
	events = input().split()[1:]
	c.update(events)
most = c.most_common(1)[0]
answer  = [k for k, v in c.most_common() if v == most[1]]
answer = reversed(answer)
print(' '.join(list(answer)))