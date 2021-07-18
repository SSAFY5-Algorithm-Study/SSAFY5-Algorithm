# 2018 KAKAO BLIND RECRUITMENT : 추석 트래픽

from datetime import datetime, timedelta
ONE_MILLISECOND = timedelta(milliseconds=1)
ONE_SECOND = timedelta(seconds=1)


def get_count(start, timeline):
    count = 0
    end = start + ONE_SECOND
    for n_start, n_end in timeline:
        if n_start < end and n_end >= start:
            count += 1
    return count


def solution(lines):
    timeline = []
    for line in lines:
        s, t = line[11:-1].split()
        s = datetime.strptime(s, '%H:%M:%S.%f')
        t = timedelta(seconds=float(t))
        timeline.append((s-t+ONE_MILLISECOND, s))

    max_count = 1
    for start, end in timeline:
        count1 = get_count(start, timeline)
        count2 = get_count(end, timeline)
        max_count = max(max_count, count1, count2)
    
    return max_count
