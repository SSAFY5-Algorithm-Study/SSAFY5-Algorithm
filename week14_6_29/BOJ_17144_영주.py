# 17144. 미세먼지 안녕! (골드5)

import sys
from collections import deque
input = sys.stdin.readline
DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1] # 상, 하, 좌, 우


# 미세먼지 확산
def diffuse(dusts):
    visited = [[0]*c for _ in range(r)]
    queue = deque(dusts)
    while queue:
        x, y = queue.popleft()
        count = 0
        for i in range(4):
            nx, ny = x+DX[i], y+DY[i]
            if 0 <= nx < r and 0 <= ny < c and house[nx][ny] != -1:
                visited[nx][ny] += (house[x][y] // 5)
                count += 1
        visited[x][y] -= (house[x][y]//5) * count

    for i in range(r):
        for j in range(c):
            house[i][j] += visited[i][j]


# 공기청정기 작동
def purify(purifier_x, count, moving):
    prev_dust = 0
    direction = 0
    tx, ty = purifier_x, 1
    while count >= 0:
        house[tx][ty], prev_dust = prev_dust, house[tx][ty]
        dx, dy = moving[direction]
        if tx+dx < 0 or tx+dx >= r or ty+dy < 0 or ty+dy >= c:
            direction += 1
            if direction >= 4:
                direction = 0
            dx, dy = moving[direction]
        tx += dx
        ty += dy
        count -= 1


r, c, t = map(int, input().split())
house = []
up, down = -1, -1 # 위쪽, 아래쪽 공기청정기의 행 번호
for i in range(r):
    line = list(map(int, input().split()))
    house.append(line)
    for j in range(c):
        if line[j] == -1 and up < 0:
            up, down = i, i+1

up_count, down_count = (up+c-2)*2, (r-down+c-3)*2
up_moving = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 위쪽 공기청정 방향 (우, 상, 좌, 하)
down_moving = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 아래쪽 공기청정 방향 (우, 하, 좌, 상)

for _ in range(t):
    dusts = [(i, j) for i in range(r) for j in range(c) if house[i][j] > 0]
    diffuse(dusts)
    purify(up, up_count, up_moving)
    purify(down, down_count, down_moving)
    
total_dust = sum(sum(line) for line in house) + 2 # 공기청정기가 '-1' 영역이므로, 이로 인해 감소된 2를 더함
print(total_dust)
