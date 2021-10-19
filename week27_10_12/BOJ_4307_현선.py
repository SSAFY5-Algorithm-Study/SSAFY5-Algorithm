# _ 1 _ _ _ 2 3 _ _ _

# 사이 간격이 홀수면 우짜냐....
# 개미1 : 최소-2 최대-8
# 개미2 : 최소-4 최대-6
# 개미3 : 최소-3 최대-7

# 빠른 시간 : 더 가까운데로 떨어지면 됨.
# 느린시간 : 그냥 젤 먼데로 가서 떨어지면 됨.


T = int(input())
for _ in range(T):
    l, n = map(int,input().split())
    ants = []
    for i in range(n):
        ants.append(int(input()))
    
    min_time = 0
    max_time = 0
    for ant in ants:
        if l-ant < ant:
            ant_min_time = l-ant
            ant_max_time = ant
        else:
            ant_min_time = ant
            ant_max_time = l-ant
        if ant_min_time > min_time:
            min_time = ant_min_time
        if ant_max_time > max_time:
            max_time = ant_max_time
    print(min_time, max_time)
        