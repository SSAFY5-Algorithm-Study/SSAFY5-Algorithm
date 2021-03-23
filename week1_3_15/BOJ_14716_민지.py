import sys
sys.stdin = open('14716_input.txt', 'r')

N, M = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(N)]

drc = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

visited = [[0]*M for _ in range(N)]

cnt = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        stack = []
        if canvas[i][j] == 1 and not visited[i][j]:
            stack.append([i, j])
            visited[i][j] = 1
            while stack:
                cr, cc = stack.pop()
                visited[cr][cc] = 1
                for dr, dc in drc:
                    nr, nc = cr+dr, cc+dc
                    if canvas[nr][nc] == 1 and not visited[nr][nc]:
                        stack.append([nr, nc])
                        visited[nr][nc] = 1
            cnt += 1
print(cnt)