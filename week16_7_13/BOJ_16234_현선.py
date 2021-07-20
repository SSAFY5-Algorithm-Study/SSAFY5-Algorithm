def move(arr,people,nation):
    p = int(people/nation)
    for n in arr:
        # 얘를 바로 해야하나?
        # 아니면 copy해놓고 바꾸고 다시 넣어줘야하나...
        nations[n[0]][n[1]] = p
    

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def BFS(r,c):
    global united
    global flag
    q = [[r,c]]
    visited[r][c] = united
    united_list = [[r,c]]
    total_people = nations[r][c]
    total_nation = 1
    # 국경선 열기
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(nations[nr][nc] - nations[cr][cc]) <= R:
                    total_people += nations[nr][nc]
                    total_nation += 1
                    visited[nr][nc] = united
                    q.append([nr,nc])
                    united_list.append([nr,nc])
    # 인구 이동하기.
    if len(united_list) >= 2:
        move(united_list, total_people, total_nation)
    else:
        flag += 1
    united += 1


N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
united = 1
day = 0
while True:
    flag = 0
    visited = [[0] * N for _ in range(N)]
    day += 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i,j)
    if flag == N * N:
        break
print(day-1)