# 막차를 탑승해야되는 사람이 여러명이라면 언제 대기해야될지 알려주는 함수
def find_makcha_time(passengers, n, m, t):
    i = 0 # 현재 탑승할 승객
    
    for j in range(n): # 셔틀
        cnt = 0 # 현재 셔틀에 탑승한 승객 수
        shuttle_time = 540 + t * j # 현재 셔틀 시간
        # 아직 셔틀이 남아있고 탈 손님이 남아있다면
        while cnt < m and i < len(passengers):
            if passengers[i] <= shuttle_time:
                cnt += 1
                i += 1
            else:
                break

    # 마지막 셔틀까지 다 돌았을때
    # cnt = 마지막 셔틀에 탑승한 승객 수
    # shuttle_time = 마지막 셔틀이 떠난 시각

    # 마지막 셔틀이 꽉 찼을 경우 마지막 손님보다 1분 먼저 도착해야 함
    if cnt == m:
        return passengers[i-1] - 1
    
    # 막차 시간에 맞춰서 탑승
    return shuttle_time
            

def solution(n, t, m, timetable):
    # 계산의 편의성을 위해 분으로 환산해서 계산한다
    # 1-1. 시간을 분으로 변환한다 
    timetable = [int(time[0:2]) * 60 + int(time[3:5]) for time in timetable]
    # 1-2. 도착하는 크루를 시간 순서대로 정렬한다
    timetable.sort()
    
    # 2. 막차를 타야되는 사람이 m명 이상일 경우 그 인원들 중 m번째 사람보다 적어도 1분 이상 먼저 도착해야한다
    passengers = timetable[:(m*n)] if len(timetable) >= (m*n) else timetable
    answer = find_makcha_time(passengers, n, m, t)

    hr, mn = divmod(answer, 60)
    answer = str(hr).zfill(2) + ":" + str(mn).zfill(2)
    return answer



"----------------------------------------------------------------------------------------------"



def convert_time(time):
    return int(time[0:2]) * 60 + int(time[3:5])

# 막차를 타야하는 사람중 첫번째 사람의 인덱스를 알려준다
def find_makcha_idx(timetable, t):
    start = 0
    end = len(timetable) - 1
    mid = (start + end) // 2 

    while start <= end:
        mid = (start + end) // 2  
        if convert_time(timetable[mid]) <= t:
            start = mid + 1
        else:
            end = mid - 1
    
    if convert_time(timetable[mid]) <= t:
        mid += 1
        
    return mid
    
def solution(n, t, m, timetable):
    # 0. 도착하는 크루를 시간 순서대로 정렬한다
    timetable.sort()
    
    # 계산의 편의성을 위해 분으로 환산해서 계산한다
    # 1. 마지막 버스가 도착하는 시간보다 같거나 먼저 나와있어야 한다
    answer = 540 + (n-1) * t
    
    # 2. n*m 번째 위치에 서있는 사람보다 적어도 1분이상 먼저 나와있어야 한다
    if len(timetable) >= (n*m):
        answer = min(answer, convert_time(timetable[n*m-1])-1)
    
    # 3. 무조건 막차를 타야되는 사람이 m명 이상일 경우 그 인원들 중 m번째 사람보다 적어도 1분 이상 먼저 도착해야한다
    # 막차 바로 전 버스의 출발시간
    penult_bus = 540 + (n-2) * t if n >= 2 else 0
    passengers = timetable[:(m*n)] if len(timetable) >= (m*n) else timetable
    if len(passengers) >= m:
        idx = find_makcha_idx(passengers, penult_bus)
        if idx <= len(passengers) - m:
            answer = min(answer, convert_time(passengers[idx+m-1])-1)
    
    hr, mn = divmod(answer, 60)
    answer = str(hr).zfill(2) + ":" + str(mn).zfill(2)
    return answer