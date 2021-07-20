'''
아이디어 ->
모든 요소를 돌면서, BFS를 통해 국경선을 열 수 있는 나라를 찾아내서 국경선을 열어주고 다시 처음부터 돌아가서 확인을 해준다.
'''
from collections import deque

dxy = [(-1,0),(1,0),(0,-1),(0,1)]

# 인구이동 가능한 나라들 확인해주는 함수
def BFS(i, j):
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    temp = []
    temp.append([i, j])
    while q:
        cr, cc = q.popleft()
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    # 두 나라의 인구차이가 L과 R사이라면 국경선을 열어준다
                    if L <= abs(arr[cr][cc] - arr[nr][nc]) <= R:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        temp.append([nr, nc])
    return temp



N, L, R = map(int, input().split())
# 나라 정보 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 인구 이동 횟수 초기화
cnt = 0

# 인구 이동이 불가능할때까지 반복
while True:
    # 방문여부 체크
    visited = [[0]*N for _ in range(N)]
    # 인구이동 여부 체크 flag
    flag = False
    # 배열의 모든 요소 탐색 - 한 번의 인구 이동에서 가능한 모든 요소 탐색
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                # 인구이동이 가능한 나라들 배열 반환
                connected_countries = BFS(i, j)
                if len(connected_countries) > 1:
                    flag = True
                    # 평균값
                    average = sum(arr[x][y] for x, y in connected_countries)//len(connected_countries)
                    # 인구이동 나라들 = 평균값
                    for x, y in connected_countries:
                        arr[x][y] = average
    # 인구이동 불가능하면
    if not flag:
        # 종료
        break
    # 인구이동 + 1
    cnt += 1

print(cnt)
