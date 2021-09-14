"""
(0,0) --> (1,1): 1
(0,0) --> (2,2): 2
(0,0) --> (3,3): 5
(0,0) --> (4,4): 14
(0,0) --> (5,5): 42

col > row것은 쓰지 않는다
"""
from copy import deepcopy

start, end = map(int, input().split())
n = abs(start-end) + 2

def find_num_paths(start, end):

    if start == end:
        return 1

    DP = [[0] * n for _ in range(n)]
    DP[0][1] = 1
    visited = deepcopy(DP)

    # 왼쪽과 위 테두리 방문 처리 하기
    for i in range(n):
        visited[0][i] = visited[i][0] = visited[n-1][i] = visited[i][n-1] = 1

    queue = [[1,1]]
    visited[1][1] = 1
    dr = [1, 0]
    dc = [0, 1]

    while queue:
        row, col = queue.pop(0)
        DP[row][col] = DP[row-1][col] + DP[row][col-1]

        for i in range(2):
            if not visited[row+dr[i]][col+dc[i]] and col <= row:
                visited[row+dr[i]][col+dc[i]] = 1
                queue.append([row+dr[i], col+dc[i]])
    
    return DP[n-2][n-2]

print(find_num_paths(start, end))