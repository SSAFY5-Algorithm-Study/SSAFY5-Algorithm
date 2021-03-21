import sys
sys.stdin = open('input.txt')

# 델타
dxy = [(-1, 0), (1, 0), (0,  1), (0, -1)]


# 시작점 찾아주는 함수
def find_start():
    global height, width
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if pic[i][j] == 1:
                if pic[i - 1][j] != 1:
                    if pic[i][j - 1] != 1:
                        st_points.append((i, j))

# DFS로 그림 개수와 최대 넓이 구하는 함수
def DFS(start, a):
    global max_value
    stack = [start]
    while stack:
        cr, cc = stack.pop()
        a += 1
        visited[cr][cc] = a
        if a > max_value:
            max_value = a
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if pic[nr][nc] == 1 and not visited[nr][nc]:
                DFS((nr, nc), a)
    return max_value

# 세로, 가로
height, width = map(int, input().split())
# 2로 패딩
pic = [[2] + list(map(int, input().split())) + [2] for _ in range(height)]
pic.insert(0, [2] * (width + 2))
pic.append([2] * (width + 2))
# 시작점 리스트 생성
st_points = []
# 시작점 찾기
find_start()
# 방문했는 지 여부 리스트 생성
visited = [[0] * (width + 2) for _ in range(height + 2)]
# 그림 최대 넓이 리스트 생성
ans = []
# DFS 진행
for point in st_points:
    max_value = -987654321
    area = 0
    ans.append(DFS(point, area))
print('%d\n%d' % (len(st_points), max(ans) if st_points else 0))