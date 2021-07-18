# 16234. 인구 이동 (골드5)

import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    total, points = population[x][y], [(x, y)]
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                population_difference = abs(
                    population[x][y]-population[nx][ny])
                if (not visited[nx][ny]) and (left <= population_difference <= right):
                    total += population[nx][ny]
                    points.append((nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return total, points


n, left, right = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
days = 0

while True:
    is_unified = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                total, points = bfs(i, j)
                if len(points) > 1:
                    is_unified = True
                    union = total // len(points)
                    for x, y in points:
                        population[x][y] = union
    if not is_unified:
        break
    days += 1

print(days)
