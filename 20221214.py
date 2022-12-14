def solution(board):
    hist = []
    N, M = len(board), len(board[0])
    def bfs(origin):
        x,y  = origin
        board[x][y]=0
        xs, ys = [0,1,1], [1,0,1]
        for dx, dy in zip(xs, ys):
            nx = x+dx
            ny = y+dy
            if nx >= N or ny >=M:
                break
            if board[nx][ny]==0:
                break
            if dx*dy==1:
                hist.append((x,y))
                bfs((x+1,y))
                bfs((x,y+1))
                bfs((x+1,y+1))
    answer = []
    for i in range(N):
        for j in range(M):
            if board[i][j]==1:
                bfs((i,j))
                while hist:
                    x,y = hist.pop()
                    if x-i == y-j:
                        answer.append(x-i)
                hist = []                
    
    answer = max(answer)+2
#     import re
#     def get_seq(row):
#         '''finds all sequences of 1s'''
#         row = ''.join(map(str, row))
#         m = re.search('1+', row)
#         return m.span()
    
#     lens = [get_seq(row) for row in board]
#     answers = []
#     for i, span in enumerate(lens):
#         s, e = span
#         l = e-s
#         minh, minv = 1000, 1000
#         for j in range(1, l):
#             if i+j < len(lens):
#                 sj, ej = lens[i+j]
#                 if sj > e or ej < s:
#                     break
#                 h = min(e, ej)-max(s, sj)
#                 minh = min(minh, h) 
#                 if i+j == i+l-1:
#                     answers.append(minh)     
#             else:
#                 break
                
#     answer = max(answers)
    return answer**2
