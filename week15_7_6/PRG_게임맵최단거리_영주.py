# Level 2 : 게임 맵 최단거리

from collections import deque


def solution(maps):
    r, c = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    visited = [[0]*c for _ in range(r)]
    visited[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                if nx == r-1 and ny == c-1:
                    return visited[nx][ny]
                queue.append((nx, ny))

    return -1