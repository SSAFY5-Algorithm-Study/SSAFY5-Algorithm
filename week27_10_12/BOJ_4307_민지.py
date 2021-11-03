from copy import copy
T = int(input())

def shortest_time(ants, l, mid):
    max_time = 0

    for i in ants:
        time = i if i <= mid else l - i
        max_time = max(max_time, time)
    return max_time


def longest_time(ants, mid, l, n):
    stick = [0] * l
    for i in range(len(ants)):
        direction = 1 if ants[i] <= mid else -1
        stick[ants[i]] = direction
    
    time = 0
    cnt = 0
    while cnt < n:
        temp = 0
        for i in range(l):
            if stick[i] == 1:
                if stick[i+1] == 0:
                    stick[i], stick[i+1] = 0, 1
                else:
                    temp = stick[i]
            elif stick[]
    print(stick)
    
    

for _ in range(T):
    l, n = map(int, input().split())
    mid = l // 2
    ants = [int(input()) for _ in range(n)]
    print(shortest_time(ants, l, mid))
    longest_time(ants, mid, l, n)

    
    