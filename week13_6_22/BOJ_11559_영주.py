# 11559. Puyo Puyo (골드5)

import sys
from collections import deque
input = sys.stdin.readline
DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]
ROW, COLUMN = 12, 6
SPACE = '.'


def find_puyo_chains(x, y):
    visited[x][y] = True
    puyo_chains = [(x, y)]
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + DX[i], y + DY[i]
            if 0 <= nx < ROW and 0 <= ny < COLUMN and not visited[nx][ny] and field[x][y] == field[nx][ny]:
                visited[nx][ny] = True
                puyo_chains.append((nx, ny))
                queue.append((nx, ny))
    return puyo_chains


def pop_puyos(puyo_chains_group):
    for puyo_chains in puyo_chains_group:
        for i, j in puyo_chains:
            field[i][j] = SPACE


def drop_puyos():
    for j in range(COLUMN):
        puyos = []
        for i in range(ROW):
            if field[i][j] != SPACE:
                puyos.append(field[i][j])
        for i in range(ROW-1, -1, -1):
            if puyos:
                field[i][j] = puyos.pop()
            else:
                field[i][j] = SPACE


field = [list(input().rstrip()) for _ in range(ROW)]
count = 0

while True:
    visited = [[False]*COLUMN for _ in range(ROW)]
    is_end = True
    puyo_chains_group = []
    for i in range(ROW):
        for j in range(COLUMN):
            if field[i][j] != SPACE:
                puyo_chains = find_puyo_chains(i, j)
                if len(puyo_chains) < 4:
                    continue # 4개 미만으로 연결된 뿌요는 터뜨리지 못함
                is_end = False
                puyo_chains_group.append(puyo_chains)
    if is_end:
        break # 터뜨릴 뿌요가 없다면 종료
    pop_puyos(puyo_chains_group)
    drop_puyos()
    count += 1

print(count)
