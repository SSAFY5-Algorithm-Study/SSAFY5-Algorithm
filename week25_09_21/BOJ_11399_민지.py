"""
# 문제 해결 방법 #
대기 시간이 긴 사람이 대기 줄의 앞쪽에 서있다면 모든 사람의 대기 시간이 늘어나게됨
대기 시간이 짧은 순서대로 ATM을 이용하도록 정렬
"""
N = int(input())
times = list(map(int, input().split()))
times.sort()

wait = 0 # 현재 사람이 대기 해야 하는 시간
total = 0 # 전체 대기 시간

for time in times:
    wait += time
    total += wait

print(total)
