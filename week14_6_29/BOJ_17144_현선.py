# 집 -> R X C
# 공기청정기 -> 항상 1번열. 크기 -> 두 행
# 공기 순환 방향 -> 청정기위쪽 : 반시계 방향 위로, 청정기 아래쪽 : 시계방향 아래쪽
# 확산은 미세먼지가 있는 모든 칸에서 동시에 일어남.

# 계산되는 배열을 따로 만들어서 해야할듯 -> 동시에 일어나는것을 반영하기위해서??

import copy
r,c,t = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(r)]
up = []
down = []
# 1단계. 먼지 옮기기.
# 상,하,좌,우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for T in range(t):
    dust_move = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 공기청정기 위치 저장하기.
            if room[i][j] == -1:
                if up:
                    down = [i,j]
                else:
                    up = [i,j]
            # 먼지가 있는 칸
            if room[i][j] != 0 and room[i][j] != -1:
                # 먼지 확산
                total_dust_diffuse = 0 # 확산된 먼지 양
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # 배열의 범위를 벗어나지 않고, 공기청정기가 아닌 경우 확산!
                    if 0 <= nr < r and 0 <= nc < c and room[nr][nc] != -1:
                        dust_diffuse = room[i][j] // 5
                        # 확산되는 칸에 이미 먼지가 있을 수 있다.
                        dust_move[nr][nc] += dust_diffuse
                        total_dust_diffuse += dust_diffuse
                # 원래 먼지가 있는 칸은 원래 있던 양에 확산된 양만큼 빼줌. 근데, 이미 확산되어 있는 먼지가 있을수도 있으니 더해줌.
                dust_move[i][j] += room[i][j] - total_dust_diffuse
    # ---------------------여기까지 매우 좋다. 문제없음.
    dust_move[up[0]][up[1]] = -1
    dust_move[down[0]][down[1]] = -1

    # 2단계. 공기청정기 작동(위쪽)
    i,j = up[0] - 1, up[1]
    # 옮겨야하니까, 배열을 새로 안만들고 값만 바꾸려면 진행방향과 반대로 진행하면 됨.
    # 즉, 원래라면 우, 상, 좌, 하 겠지만. 상, 우, 하, 좌 순으로 진행.
    for k in range(4):
        # 위로~~
        if k == 0:
            while i != 0:
                if i + 1 == up[0]:
                    dust_move[i][j] = 0
                else:
                    dust_move[i+1][j] = dust_move[i][j]
                i -= 1
            dust_move[i+1][j] = dust_move[i][j]
            dust_move[i][j] = 0
        # 오른쪽으로 ~~
        elif k == 1:
            j = 1
            while j != c-1:
                dust_move[i][j-1] = dust_move[i][j]
                j += 1
            dust_move[i][j-1] = dust_move[i][j]
            dust_move[i][j] = 0
        # 아래로~~~
        elif k == 2:
            i = 1
            while i != up[0]:
                dust_move[i-1][j] = dust_move[i][j]
                i += 1
            dust_move[i-1][j] = dust_move[i][j]
            dust_move[i][j] = 0
        # 왼쪽으로~~
        elif k == 3:
            j = j-1
            while j != 0:
                dust_move[i][j+1] = dust_move[i][j]
                j -= 1
            dust_move[i][j+1] = 0
    # ---------------- 여기까지 굳

    # 3단계. 공기청정기 작동(아래쪽) - 사실 하나로 처리도 가능할거 같긴함.
    # 원래라면 우, 하, 좌, 상. but 난 하, 우, 상, 좌 순으로 진행.
    i,j = down[0] + 1, down[1]
    for k in range(4):
        # 아래로~~
        if k == 0:
            while i != r-1:
                if i - 1 == down[0]:
                    dust_move[i][j] = 0
                else:
                    dust_move[i-1][j] = dust_move[i][j]
                i += 1
            dust_move[i-1][j] = dust_move[i][j]
            dust_move[i][j] = 0
        # 오른쪽으로 ~~
        elif k == 1:
            j = 1
            while j != c-1:
                dust_move[i][j-1] = dust_move[i][j]
                j += 1
            dust_move[i][j-1] = dust_move[i][j]
            dust_move[i][j] = 0
        # 위로~~~
        elif k == 2:
            i = i-1
            while i != down[0]:
                dust_move[i+1][j] = dust_move[i][j]
                i -= 1
            dust_move[i+1][j] = dust_move[i][j]
            dust_move[i][j] = 0
        # 왼쪽으로~~
        elif k == 3:
            j = j-1
            while j != 0:
                dust_move[i][j+1] = dust_move[i][j]
                j -= 1
            dust_move[i][j+1] = 0
    room = copy.deepcopy(dust_move)
# print(dust_move)
# 4단계. 다 읽기.
# 이렇게 읽지 말고, room 배열에서 먼지 나눌때 값을 다 계산때려서, 공기청정기로 들어가서 없어지는 먼지들만 빼는 방법이 더 효율적일듯?
result = 0
for i in range(r):
    for j in range(c):
        if dust_move[i][j]:
            result += dust_move[i][j]
print(result+2)