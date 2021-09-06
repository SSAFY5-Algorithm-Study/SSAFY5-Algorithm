# 유효 box 크기 (1, R - 1)(1, C - 1)

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def BFS(y, x):
    queue = [(y, x)]
    visited[y][x] = 1
    while queue:
        cr, cc = queue.pop()
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if 0 <= nr <= R - 1 and 0 <= nc <= C - 1:
                if not visited[nr][nc]:
                    if box[nr][nc] == 0:
                        queue.append((nr, nc))
                    elif box[nr][nc] == 1:
                        box[nr][nc] = 0
                    visited[nr][nc] = 1


def check_cheese(R, C):
    temp = 0
    for i in range(R):
        for j in range(C):
            if box[i][j] == 1:
                temp += 1
    return temp

R, C = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(R)]

previous_cheese = check_cheese(R, C)
time_spent = 0


while True:
    visited = [[0] * C for _ in range(R)]
    print(previous_cheese, '치즈개수', box)
    for i in range(1, R):
        for j in range(1, C):
            if box[i][j] == 0 and not visited[i][j]:
                BFS(i, j)
    # print(time_spent, box)
    one_existed = check_cheese(R, C)
    if one_existed == 0:
        break
    else:
        previous_cheese = one_existed
        time_spent += 1

print('time', time_spent, 'previous', previous_cheese)