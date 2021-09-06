# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs():
    q = [[0,0]]
    # 테두리에 있는 애들만 제거하기 위한 새로운 배열
    cheeze_map = [[2] * c for _ in range(r)]
    cheeze_map[0][0] = 0
    cnt = 0
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                # print(nr,nc)
                # 테두리에 있는 애들만 1 -> 0으로 만들어주고 방문 체크.
                # 치즈가 아닌 부분은 방문체크만 하고 q에 추가.
                if cheeze_map[nr][nc]:
                    if cheeze[nr][nc]:
                        cheeze[nr][nc] = 0
                        cheeze_map[nr][nc] = 0
                        # 지운 애들 카운트
                        cnt += 1
                    else:
                        cheeze_map[nr][nc] = 0
                        q.append([nr,nc])
    return cnt

r, c = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(r)]

time = 0
before_one_hour = 0
while True:
    # print(cheeze)
    # 반환값 : 지운 치즈 테두리 갯수
    k = bfs()
    time += 1
    # 반환값이 없으면 다 지워진것 -> 우리가 얻고싶은것은 다 지워지기 직전 갯수.
    if k:
        before_one_hour = k
    else:
        break
print(time-1)
print(before_one_hour)