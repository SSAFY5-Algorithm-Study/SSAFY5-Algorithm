import sys
sys.stdin = open('1926_input.txt', 'r')

# input 받아오기 N, M, Canvas
# Canvas는 탐색하기 편하도록 주변에 벽을 둘러서 input을 받아온다
N, M = map(int, input().split())
canvas = [[-1] * (M+2)]
canvas += [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
canvas += [[-1] * (M+2)]

# for row in canvas:
#     print(row)

visited = [[0]*(M+2) for _ in range(N+2)]
# print(canvas)

drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]

max_area = 0
cnt = 0
# 탐색 중 1을 발견하면 stack에 위치를 넣고 그 위치로 부터 dfs 탐색 시작
for i in range(1, N+1):
    for j in range(1, M+1):
        stack = []
        area = 1
        if canvas[i][j] == 1 and (not visited[i][j]):
            stack.append([i, j])
            visited[i][j] = 1
            while stack:
                current = stack.pop()
                cr, cc = current
                for dr, dc in drc:
                    if not visited[cr+dr][cc+dc] and canvas[cr+dr][cc+dc] == 1:
                        stack.append([cr+dr, cc+dc])
                        visited[cr+dr][cc+dc] = 1
                        area += 1
            if area > max_area:
                max_area = area
            cnt += 1


print(cnt)
print(max_area)