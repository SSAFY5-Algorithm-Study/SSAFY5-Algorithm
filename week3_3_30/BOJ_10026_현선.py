'''
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 

그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 

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

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
'''

# 접근 : visited 배열을 2개 만들어서, 적록색맹이 아닐 경우 - 적록색맹일 경우 2가지를 따로 따로 나눈다
# 색맹인 경우 : R,G를 하나로 묶어서 생각. 탐색하는 색깔이 R이나 G인 경우와 B인 경우로 나누어 생각
# 색맹이 아닌 경우 : R,G,B를 각각 따로 계산
# 더 효율적인 방법이 있을거 같은데....... 애시당초에, 그림 배열을 2개를 만들어서 적록색맹인 경우 G를 R로 바꿔놓고 탐색해도 될듯.

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 적록색맹이 아닌 경우.
def BFS_RGB(r,c,temp_color):
    visited_RGB[r][c] = 1
    q = [[r,c]]
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 탐색하는 색깔과 같은 경우에만 visited 배열 최신화
            if 0 <= nr < N and 0 <= nc < N and visited_RGB[nr][nc] == 0 and picture[nr][nc] == temp_color:
                visited_RGB[nr][nc] = 1
                q.append([nr,nc])

# 적록색맹인 경우
def BFS_RB(r,c,temp_color):
    visited_RB[r][c] = 1
    q = [[r,c]]
    while q:
        cr, cc = q.pop(0)
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited_RB[nr][nc] == 0:
                # R,G는 하나의 색깔로 처리해야함.
                if temp_color == 'R' or temp_color == 'G':
                    if picture[nr][nc] == 'R' or picture[nr][nc] == 'G':
                        visited_RB[nr][nc] = 1
                        q.append([nr,nc])
                # B인 경우만 생각
                else:
                    if temp_color == 'B' and picture[nr][nc] == 'B':
                        visited_RB[nr][nc] = 1
                        q.append([nr,nc])


                    
N = int(input())
picture = [list(input()) for _ in range(N)]

# visited 배열을 따로 선언
visited_RGB = [[0] * N for _ in range(N)]
visited_RB = [[0] * N for _ in range(N)]

# 각각의 상황에 따른 영역 수를 따로 계산
area_RGB = 0
area_RB = 0


# picture 배열을 하나씩 확인하면서 visited 값이 0인 경우만 탐색. 각각 탐색함.
for i in range(N):
    for j in range(N):
        if visited_RGB[i][j] == 0:
            BFS_RGB(i,j,picture[i][j])
            area_RGB += 1
        if visited_RB[i][j] == 0:
            BFS_RB(i,j,picture[i][j])
            area_RB += 1

print(area_RGB, area_RB)