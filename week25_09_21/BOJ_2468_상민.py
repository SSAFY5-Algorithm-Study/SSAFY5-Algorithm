# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7



dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def BFS(s, e, standard_value):
  temp = 0
  # s, e부터 탐색
  queue = [(s, e)]
  if area[s][e] <= standard_value:
    visited[s][e] = 0
    return temp
  visited[s][e] = 1
  temp = 1
  while queue:
    cr, cc = queue.pop(0)
    for r, c in dxy:
      nr = cr + r
      nc = cc + c
      if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
        if area[nr][nc] <= standard_value:
          visited[nr][nc] = 0
          continue
        visited[nr][nc] = 1
        queue.append((nr, nc))
  return temp


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_value = max(max(area))

# 정답(영역 갯수)
max_answer = [0]
for i in range(1, max_value + 1):
  visited = [[-1] * N for _ in range(N)]
  temp = 0
  for j in range(N):
    for k in range(N):
      if visited[j][k] == -1:
        temp += BFS(j, k, i)
  max_answer[0] = max(max_answer[0], temp)

print(max_answer[0])