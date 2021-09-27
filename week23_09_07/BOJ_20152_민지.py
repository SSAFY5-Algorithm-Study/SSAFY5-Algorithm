"""
col > row것은 쓰지 않는다
col <= row라는 조건식 필요
"""
from copy import deepcopy

start, end = map(int, input().split())
n = abs(start-end) + 3

def find_num_paths(start, end):

    if start == end:
        return 1

    DP = [[0] * n for _ in range(n)]
    DP[0][1] = 1
    visited = deepcopy(DP)

    # 상하좌우 벽치기
    for i in range(n):
        visited[0][i] = visited[i][0] = visited[n-1][i] = visited[i][n-1] = 1

    # 시작점 설정
    queue = [[1,1]]
    visited[1][1] = 1
    dr = [1, 0]
    dc = [0, 1]

    while queue:
        row, col = queue.pop(0)
        DP[row][col] = DP[row-1][col] + DP[row][col-1]

        for i in range(2):
            if not visited[row+dr[i]][col+dc[i]] and col+dc[i] <= row+dr[i]:
                visited[row+dr[i]][col+dc[i]] = 1
                queue.append([row+dr[i], col+dc[i]])
    
    return DP[n-2][n-2]

print(find_num_paths(start, end))