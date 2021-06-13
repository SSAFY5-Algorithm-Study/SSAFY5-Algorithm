import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
tank = [list(map(int, input().split())) for _ in range(N)]
# 크기가 커지려면 먹어야되는 물고기의 수
size = size_up = 2
drc = [[-1, 0], [0, -1], [0, 1], [1, 0]]

# BFS로 (상,좌,우,하) 순서대로 탐색하면서 먹을 수 있는 물고기가 있는지 확인
def bfs(r, c, start_sec):
    global size, size_up
    visited = [[0]*N for _ in range(N)]
    queue = [(r, c, start_sec)]
    while queue:
        r, c, sec = queue.pop(0)
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if 1 <= tank[nr][nc] < size:
                    print(nr, nc, size, sec+1)
                    tank[nr][nc] = 0
                    size_up -= 1
                    if size_up == 0:
                        size = size_up = size + 1
                    return nr, nc, sec+1
                elif tank[nr][nc] > size:
                    continue
                else:
                    queue.append([nr, nc, sec+1])
                    visited[nr][nc] = 1
    return -1, -1, start_sec


# 시작점을 찾는다
for i in range(N):
    for j in range(N):
        if tank[i][j] == 9:
            tank[i][j] = 0
            r, c = i, j

sec = 0
while r >= 0:
    r, c, sec = bfs(r, c, sec)

print(sec)