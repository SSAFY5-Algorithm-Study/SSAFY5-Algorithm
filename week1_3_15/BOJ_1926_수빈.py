'''
1926. 그림

어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.
'''
# 상하좌우 델타값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 넓이 구하는 함수
def DFS(start_x, start_y):
    area = 1
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # paper 값이 1이고 방문하지 않았다면
                if paper[nx][ny] == 1 and not visited[nx][ny]:
                    # 방문 표시
                    visited[nx][ny] = 1
                    # 넓이 추가
                    area += 1
                    stack.append((nx, ny))
    return area

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
max_area = 0
cnt_painting = 0

# 처음부터 끝까지 돌면서
for i in range(n):
    for j in range(m):
        # paper 값이 1이고 방문한 적이 없으면
        if paper[i][j] == 1 and not visited[i][j]:
            # 방문 표시
            visited[i][j] = 1
            # 그림 개수 추가
            cnt_painting += 1
            # 넓이 최대값 구하기
            max_area = max(max_area, DFS(i, j))
            

print(cnt_painting)
print(max_area)
'''
[입력]
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

[출력]
4
9
'''