# 16236. 아기 상어 (골드4)

import sys
from collections import deque
from heapq import heappush
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    possible_fish = []
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and baby_size >= area[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if 0 < area[nx][ny] < baby_size:
                    heappush(possible_fish, (visited[nx][ny]-1, nx, ny))
    return possible_fish

n = int(input())
area = []
for i in range(n):
    line = list(map(int, input().split()))
    area.append(line)
    for j in range(n):
        if line[j] == 9:
            bx, by = i, j

baby_size, baby_eating, seconds = 2, 0, 0
while True:
    area[bx][by] = 0
    targets = bfs(bx, by)
    if not targets:
        break
    second, bx, by = targets[0]
    seconds += second
    baby_eating += 1
    if baby_eating >= baby_size:
        baby_size += 1
        baby_eating = 0
print(seconds)
