from collections import deque

def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    r = len(maps) - 1
    c = len(maps[0]) - 1
    queue = deque([(0, 0)])
    visited = [[0] * (c+1) for _ in range(r+1)]
    visited[0][0] = 1

    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < r+1 and 0 <= nc < c+1 and maps[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                if visited[r][c]:
                    return visited[r][c]
                queue.append((nr, nc))
    return -1