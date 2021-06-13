# 14500. 테트로미노 (골드5)

import sys
input = sys.stdin.readline

# dfs를 위한 방향: 하, 좌, 우 (상은 생략)
dx, dy = [1, 0, 0], [0, -1, 1]

# T모양 블록 탐색을 위한 방향
tx = [(-1, 0, 0, 1), (0, 0, 0, 1), (-1, 0, 0, 1), (-1, 0, 0, 0)]
ty = [(0, 0, 1, 0), (-1, 0, 1, 0), (0, -1, 0, 0), (0, -1, 0, 1)]


def dfs(x, y, depth, total):
    if depth >= 4:
        global max_total
        max_total = max(max_total, total)
        return
    for i in range(3):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, total+paper[nx][ny])
            visited[nx][ny] = False


def check_T_blocks(x, y):
    global max_total
    for i in range(4):
        total = 0
        for j in range(4):
            nx, ny = x+tx[i][j], y+ty[i][j]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            total += paper[nx][ny]
        else:
            max_total = max(max_total, total)


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
max_total = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = False
        check_T_blocks(i, j)
print(max_total)