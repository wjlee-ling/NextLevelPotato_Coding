def solution(lines):
    # 2nd try -> partial success
    def timer(line):
        # get start and end timestep
        _, end, dur = line.split()  
        dur_in_seconds = float(dur[:-1]) # drop 's'
        # convert end type -> num    
        end_in_seconds = sum([unit*s for unit, s in zip(map(float, end.split(":")) , [3600, 60, 1]) if unit > 0.0])
        start_in_seconds = end_in_seconds - dur_in_seconds + 1

        return start_in_seconds, end_in_seconds

    lines = [timer(line) for line in lines]
    answer = 1
    for i, (curr_s, curr_e) in enumerate(lines[:-1]):
        res = 0
        for j, (next_s, next_e) in enumerate(lines[i+1:]):
            if next_s - curr_e <= 1.0:
                res += 1
            else:
                break
        answer = max(answer, res)
    
    return answer
        
    
#     '''
#     1st try: stack -> wrong. cannot gurantee the last element of the stack has the last end timestep 
#     start/end time
#     '''
#     def timer(end, dur):
#         import math
#         # get start and end timestep
#         dur_in_seconds = float(dur[:-1]) # drop 's'
#         # convert end type -> num    
#         end_in_seconds = sum([unit*s for unit, s in zip(map(float, end.split(":")) , [3600, 60, 1]) if unit > 0.0])
#         start_in_seconds = end_in_seconds - dur_in_seconds + 1
        
#         return start_in_seconds, end_in_seconds
        
#     from collections import deque
#     lines = deque(lines)
#     curr = lines.popleft()
#     _, curr_e, dur = curr.split()
#     s, e = timer(curr_e, dur)
#     stack = [(s,e)] 
#     answer = 1
#     while lines:
#         curr = lines.popleft()
#         _, curr_e, dur = curr.split()
#         s, e = timer(curr_e, dur)
#         if stack:
#             print(stack[-1][1], s, s-stack[-1][1])
#             diff = s-stack[-1][1]
#             answer = max(answer, len(stack)+int(diff<1.0))
#         while stack and stack[-1][1] < s:
#             stack.pop()
#         stack.append((s,e))
#     return answer
