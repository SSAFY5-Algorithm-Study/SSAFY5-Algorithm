dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def BFS(start_node, target_row, target_col, maps):
    global discovered
    queue = [start_node + (1,)]
    discovered[start_node[0]][start_node[1]] = 1
    while queue:
        cr, cc, w = queue.pop(0)
        for r, c in dxy:
            nr = cr + r
            nc = cc + c
            if 0 <= nr <= target_row and 0 <= nc <= target_col and maps[nr][nc]:
                if not discovered[nr][nc]:
                    if nr == target_row and nc == target_col:
                        return w + 1
                    discovered[nr][nc] = 1
                    queue.append((nr, nc, w + 1))
    return -1
                    
    

def solution(maps):
    global discovered
    # n, m 찾기
    n = len(maps) - 1
    m = len(maps[0]) - 1
    discovered = [[0] * (m+1) for _ in range(n+1)]
    answer = BFS((0,0), n, m, maps)
    return answer