import sys
sys.stdin = open('input.txt')
# 재귀 제한 해제
limit_number = 30000
sys.setrecursionlimit(limit_number)

dxy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def DFS(rc):
    stack = [rc]
    while stack:
        r, c = stack.pop()
        visited[r][c] = 1
        for y, x in dxy:
            nr = r + y
            nc = c + x
            if board[nr][nc] == 1 and not visited[nr][nc]:
                DFS((nr, nc))


M, N = map(int, input().split())
# 2로 padding
board = [[2] + list(map(int, input().split())) + [2] for _ in range(M)]
board.insert(0, [2] * (N + 2))
board.append([2] * (N + 2))
visited = [[0] * (N + 2) for _ in range(M + 2)]
cnt = 0
# 1을 완전 탐색하면서 DFS 진행
# visited 체크 된 `1`은 건너 뛰기
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            DFS((i, j))

print(cnt)