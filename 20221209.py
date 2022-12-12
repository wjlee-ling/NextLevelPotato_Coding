import math

def solution(k, d):
    answer = 0
    
#     def get_squared_distance(x, y):
#         return x**2 + y**2
     
#     queue = [[0, 0]]
#     visited = [[0, 0]]
    
#     dx = [0, k]
#     dy = [k ,0]
    
#     while queue:
#         x, y = queue.pop(0)
        
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or ny < 0 or nx > d or ny > d or get_squared_distance(nx, ny) > d**2:
#                 continue

#             if [nx, ny] not in visited:
#                 answer += 1
#                 visited.append([nx, ny])
#                 queue.append([nx, ny])
                
    
#     print(queue, visited)
    for i in range(0, d + 1, k):
        max_y = int(math.sqrt(d**2 - i**2))
        answer += max_y // k + 1
    
    return answer