# 로그 문자열을 계산하기 쉬운 형태로 변환
# 1초 내에 속하는 개수 count

import datetime

def solution(lines):
    """
    Args:
        lines (List[str]) : 로그 문자열 "일자 hh:mm:ss.sss 걸린시간" 
                          〉["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
        answer
            초당 최대 처리량
    """
    preprocessed_logs = []
    for log in lines:
        logs = log.split(" ")
        timestamp = datetime.datetime.strptime(
            f"{logs[0]} {logs[1]}", "%Y-%m-%d %H:%M:%S.%f"
        ).timestamp()

        preprocessed_logs.append((timestamp, -1)) # 종료시간(-1)
        preprocessed_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1)) # 시작시간(1)


    count = 0
    max_count = 1
    preprocessed_logs.sort(key=lambda x: x[0])

    for i, log_1 in enumerate(preprocessed_logs):
        curr = count
        for log_2 in preprocessed_logs[i:]:
            if log_2[0] - log_1[0] > 0.999:
                break
            if log_2[1] == 1:
                curr += log_2[1]

        max_count = max(max_count, curr)
        count += log_1[1]

    return max_count