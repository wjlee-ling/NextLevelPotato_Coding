'''
lines 배열에 대한 "초당 최대 처리량"을 리턴하라
초당 최대 처리량: 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수

lines에는 응답완료 시간 S(2016-09-15, hh:mm:ss.sss)와 처리 시간 T가 공백으로 구분되어 있음
(S를 기준으로 오름차순)

ex. 2016-09-15 03:10:33.020 0.011s   
    2016년 9월 15일 오전 3시 10분 33.020초까지 "0.011초" 동안 처리된 요청
    
<idea>
기간이 겹쳤다는 걸 어떻게 확인할까
'''
# 정수형으로 시간을 변환하는 코드
def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond

# 시작 시간을 구하는 코드
def get_start_time(time, duration):
    n_time = duration[:-1]
    int_duration = float(n_time) * 1000
    return get_time(time) - int_duration + 1

def solution(lines):
    answer = 0 # 최대 처리량
    if len(lines) == 1:
        return 1
    
    start = []
    end = [] # 각 로그가 끝나는 시간을 변환한 값을 저장
    
    for task in lines:
        date, time, duration = task.split()
        # print(date, time, duration)
        start.append(get_start_time(time, duration)) # 별도로 시간 변환 안함
        end.append(get_time(time))
    
    for i in range(len(lines)):
        cnt = 0 # 각 시간마다 처리되는 로그 개수
        cur_end_time = end[i] # 뒤의 로그와 비교
        for j in range(i, len(lines)):
            if cur_end_time > start[j]- 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer