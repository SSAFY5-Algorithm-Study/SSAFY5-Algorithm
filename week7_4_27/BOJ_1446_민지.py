# BOJ 1446 지름길
"""
접근법
1. 지름길을 시작 위치 기준으로 오름차순 정렬한다
2. idx 칸까지 가기 위한 최소 거리를 저장한 배열 min_dist를 만든다
3. idx를 한칸씩 이동하면서, 현재 min_dist에 저장되어있는 값과 이전칸에서 한칸 더 이동했을때 두가지 경우 중 최소 값을 구한다
4. 현재 위치에서 출발할 수 있는 지름길이 있는지 검사한다
5. 현재 위치에서 이동할 수 있는 지름길이 있다면 min_dist[end]에 현재 저장되어 있는 값과 비교하여 더 짧은 지름길로 이동한다
6. 도착지에 도착할때까지 반복한다

"""
import sys
sys.stdin = open('input.txt')

N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort()

min_dist = [10001] * (D+1)
min_dist[0] = 0
# 현재 위치
idx = 0
# 현재 위치까지의 최소거리
temp_min = 0

while idx <= D:
    # print(idx, temp_min)
    temp_min = min_dist[idx] = min(min_dist[idx], temp_min+1)
    for shortcut in shortcuts:
        s, e, d = shortcut
        if s == idx and e <= D:
            min_dist[e] = min(min_dist[e], temp_min+d)

    idx += 1

print(min_dist[D])