'''
16236. 아기상어

N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 
물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
'''
from collections import deque
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    eat = []
    dist = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append([x, y])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visit[nr][nc] == 0:
                if s[nr][nc] <= s[x][y] or s[nr][nc] == 0:
                    queue.append([nr, nc])
                    visit[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + 1
                if s[nr][nc] < s[x][y] and s[nr][nc] != 0:
                    eat.append([nr, nc, dist[nr][nc]])
    if not eat:
        return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1]))
    return eat[0]

n = int(input())
s = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:
            s[i][j] = 2
            start = [i, j]
exp = 0
second = 0
while True:
    i, j = start
    ex, ey, dist = bfs(i, j)
    if ex == -1: 
        break
    s[ex][ey] = s[i][j]
    s[i][j] = 0
    start = [ex, ey]
    exp += 1
    if exp == s[ex][ey]:
        exp = 0
        s[ex][ey] += 1
    second += dist
print(second)

'''
[입력]
3
0 0 1
0 0 0
0 9 0

[출력]
3
'''