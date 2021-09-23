n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    q = [[r,c]]
    visited[r][c] = 1
    while q:
        cr,cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr <n and 0 <= nc < n and not chimsoo[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append([nr,nc])
    
rain = 1
highst_no_chimsoo_value = 1
while True:
    no_chimsoo = 0
    chimsoo = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] <= rain:
                chimsoo[i][j] = 1

    for i in range(n):
        for j in range(n):
            if not chimsoo[i][j] and not visited[i][j]:
                no_chimsoo += 1
                BFS(i,j)
    if not no_chimsoo:
        break
    if highst_no_chimsoo_value < no_chimsoo:
        highst_no_chimsoo_value = no_chimsoo
    rain += 1 
print(highst_no_chimsoo_value)