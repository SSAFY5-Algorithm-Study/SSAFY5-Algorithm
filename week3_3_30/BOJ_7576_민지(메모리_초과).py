import sys
from collections import deque
sys.stdin = open('7576_input.txt', 'r')

C, R = map(int, input().split())
box = [[-1] + list(map(int, input().split())) + [-1] for _ in range(R)]
box.insert(0, [-1] * (C+2))
box.append([-1] * (C+2))
queue = deque()

visited = [[1] + [0]*C + [1] for _ in range(R)]
visited.insert(0, [1] * (C+2))
visited.append([1] * (C+2))

for i in range(1, R+1):
    for j in range(1, C+1):
        if box[i][j]==1:
            visited[i][j] = 1
            queue.append((i, j))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
days = -1

total = 0
for i in range(1, R+1):
    for j in range(1, C+1):
        if box[i][j] == -1:
            visited[i][j] = 1
        else:
            total += 1

cnt = 0
while queue:
    days += 1
    new_queue = deque()
    for tomato in queue:
        cr, cc = tomato[0], tomato[1]
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if visited[nr][nc] == 0 and box[nr][nc] == 0:
                visited[cr][cc] = 1
                new_queue.append((nr, nc))
                cnt += 1
    queue = new_queue

if cnt != total:
    print(-1)
        
else:
    print(days)