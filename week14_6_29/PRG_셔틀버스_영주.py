# 2018 KAKAO BLIND RECRUITMENT : [1차]셔틀버스

from collections import deque
from datetime import datetime, timedelta


# string -> datetime
def get_time(time_string):
    return datetime.strptime(time_string, '%H:%M')


# datetime -> string
def get_string(time_datetime):
    return time_datetime.strftime('%H:%M')


def solution(n, t, m, timetable):
    timetable = deque(sorted(timetable))
    start = get_time('09:00')
    term = timedelta(minutes=t)
    last_crew = None

    for i in range(n): # 셔틀
        for j in range(m): # 좌석
            if not timetable:
                last_start = start + ((n-i-1) * term)
                return get_string(last_start) # 좌석 혹은 셔틀이 남은 경우, 막차를 타면 된다.
            next_crew = get_time(timetable[0])
            if next_crew > start:
                if i == n-1 and j < m:
                    return get_string(start) # 막차인데 좌석이 남은 경우 막차 시간에 맞춰서 탄다.
                break # 해당 시간에 더이상 탈 수 있는 크루가 없다면, 다음 셔틀로 넘어간다.
            last_crew = get_time(timetable.popleft())
        start += term

    if not last_crew:
        return get_string(start-term)
    else:
        return get_string(last_crew-timedelta(minutes=1))


print(solution(2,10,3,["09:05","09:09","09:13"])) # 굉장히 중요한 반례