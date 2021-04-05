'''
10026. 적록색약

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(x, y):
    visited[x][y] = 1
    queue = [(x, y)]
    color = colors[x][y]
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and colors[nr][nc] == color:
                visited[nr][nc] = 1
                queue.append((nr, nc))


N = int(input())
colors = [list(input()) for _ in range(N)]

# 적록색약 아닌 사람 방문체크
# visited1 = [[0] * N for _ in range(N)]
# # 적록색약인 사람 방문 체크
# visited2 = [[0] * N for _ in range(N)]
# 두 개 만들면 BFS 함수 안에서 또 분기처리 해야 한다.
# 그냥 구역 수 하나 구하고 초기화한 후에 다시 구하기.

# 방문 횟수
visited = [[0] * N for _ in range(N)]
# 적록색약 아닌 사람이 봤을 때 구역수
cnt = 0
# 방문하지 않았을 경우 BFS 탐색
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt += 1


# G를 모두 R로 변환한 후 BFS 탐색
for i in range(N):
    for j in range(N):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'
# 적록색약인 사람이 봤을 때 구역 수
cnt_RG = 0
# 방문 횟수 초기화
visited = [[0] * N for _ in range(N)]
# 방문하지 않았을 경우 BFS 탐색
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt_RG += 1

print(cnt, cnt_RG)

'''
[입력]
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

[출력]
4 3
'''