import sys
sys.stdin = open('14716_input.txt', 'r')

drc = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def DFS(cr, cc):
    visited[cr][cc] = 1
    stack = [(cr, cc)]
    while stack:
        cr, cc = stack.pop()
        for dr, dc in drc:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc <= M:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    if canvas[nr][nc] == 1:
                        stack.append((nr, nc))
                    

N, M = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if canvas[i][j] == 1 and not visited[i][j]:
            DFS(i, j)
            cnt += 1
print(cnt)