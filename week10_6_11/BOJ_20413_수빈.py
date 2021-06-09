'''
20413. MVP 다이아몬드(Easy)

https://www.acmicpc.net/problem/20413
'''
N = int(input())
# 등급 기준액
s, g, p, d = map(int, input().split())
ranks = input()

base = {'B': s, 'S': g, 'G': p, 'P': d}
max_cost = 0
last = 0

for rank in ranks:
    # 최고 등급이면 바로 더해준다.
    if rank == 'D':
        max_cost += base['P']
    else:
        last += (base[rank] - 1) - last
        max_cost += last
    # print(last)
print(max_cost)

'''
[입력]
3
30 60 90 150
BSG

[출력]
118
'''