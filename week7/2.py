'''
N 명의 친구(1~N번)와 M 쌍의 친구 관계 (양방향 친구)
1번 친구한테 소문을 퍼뜨렸을 때 소문을 듣게 될 친구가 몇 명?

idea : 서로소 집합을 활용한 사이클 판별(같은 팀인지 파악)
***** 노드 수 세는 걸 모르겠음. 맞게 푼 건지 모르겠음
'''
from collections import Counter

#import sys
#sys.stdin = open('./quiz/input2.txt', 'r')

def find_parent(parent, x): # x의 부모 (속한 집합) 찾기
    if parent[x] != x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)   
    if a > b:
        parent[b] = a # 1과 2가 연결되어 있으면 parent[2] = 1
        for i in range(len(parent)):
            if parent[i] == b:
                parent[i] = a
    else:
        parent[a] = b
        for i in range(len(parent)):
            if parent[i] == a:
                parent[i] = b

N = int(input()) # 노드의 개수
M = int(input()) # 간선의 개수
parent = [0]*(N+1) # 부모 테이블 초기화

for i in range(1, N+1):
    parent[i] = i # 부모 테이블 자기 자신으로 설정
#print(parent)

answer = 0
for i in range(M):
    a, b = map(int, input().split())
    #print(parent)
    if find_parent(parent, a) == find_parent(parent, b):
        break
    else:
        union_parent(parent, a,b)

print(parent)
print(Counter(parent))
for num in Counter(parent).values():
    if num >= 3:
        answer += num
print(answer)
